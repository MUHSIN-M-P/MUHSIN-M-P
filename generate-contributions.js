const fs = require("fs");
const axios = require("axios");
require("dotenv").config();

const username = "MUHSIN-M-P";
const token = process.env.GITHUB_TOKEN;
const readmePath = "README.md";
const cachePath = ".cache.json";

const headers = {
  Authorization: `token ${token}`,
  "User-Agent": "GitHub-Contrib-Script",
  Accept: "application/vnd.github+json"
};

if (!token) throw new Error("❌ GITHUB_TOKEN is not set in environment variables.");

function loadCache() {
  if (fs.existsSync(cachePath)) return JSON.parse(fs.readFileSync(cachePath, "utf8"));
  return {};
}

function saveCache(cache) {
  fs.writeFileSync(cachePath, JSON.stringify(cache, null, 2));
}

function formatCommits(commits) {
  return Object.values(commits)
    .sort((a, b) => new Date(b.date) - new Date(a.date))
    .map(
      c =>
        `- [${c.repo} \`${c.sha.slice(0, 7)}\`](${c.url}): ${c.message} (${new Date(c.date).toLocaleDateString()})`
    )
    .join("\n");
}

async function fetchEvents(page = 1) {
  const url = `https://api.github.com/users/${username}/events?page=${page}&per_page=100`;
  const { data } = await axios.get(url, { headers });
  return data;
}

async function fetchAllRecentEvents() {
  const events = [];
  for (let page = 1; page <= 3; page++) {
    const pageEvents = await fetchEvents(page);
    if (!pageEvents.length) break;
    events.push(...pageEvents);
  }
  return events;
}

async function generateReadmeSection() {
  const cache = loadCache();
  const events = await fetchAllRecentEvents();
  const updates = {};

  for (const event of events) {
    if (event.type === "PushEvent" && event.payload?.commits?.length) {
      const repo = event.repo.name;
      const latestCommit = event.payload.commits.slice(-1)[0];
      const url = `https://github.com/${repo}/commit/${latestCommit.sha}`;
      const commitData = {
        repo,
        sha: latestCommit.sha,
        message: latestCommit.message,
        date: event.created_at,
        url
      };
      if (!cache[repo] || new Date(commitData.date) > new Date(cache[repo].date)) {
        updates[repo] = commitData;
      }
    }
  }

  const updatedCache = { ...cache, ...updates };
  saveCache(updatedCache);

  const section = `<!--START_CONTRIBUTED_REPOS-->\n## 🔥 Latest Commit per Contributed Repo\n${formatCommits(updatedCache)}\n<!--END_CONTRIBUTED_REPOS-->`;
  const readme = fs.readFileSync(readmePath, "utf8");
  const newReadme = readme.replace(/<!--START_CONTRIBUTED_REPOS-->[\s\S]*<!--END_CONTRIBUTED_REPOS-->/, section);

  fs.writeFileSync(readmePath, newReadme);
  console.log("✅ README updated with recent contributions.");
}

generateReadmeSection().catch(err => console.error("❌ Failed:", err.message));
