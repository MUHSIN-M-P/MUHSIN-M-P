const fs = require("fs");
const axios = require("axios");
require("dotenv").config();

const username = "MUHSIN-M-P";
const token = process.env.GITHUB_TOKEN;
const readmePath = "README.md";
const cachePath = ".cache.json";

const headers = {
  ...(token ? { Authorization: `token ${token}` } : {}),
  "User-Agent": "GitHub-Contrib-Script",
  Accept: "application/vnd.github+json"
};

function loadCache() {
  if (fs.existsSync(cachePath)) {
    try {
      return JSON.parse(fs.readFileSync(cachePath, "utf8"));
    } catch (e) {
      return {};
    }
  }
  return {};
}

function saveCache(cache) {
  fs.writeFileSync(cachePath, JSON.stringify(cache, null, 2));
}

function formatDate(dateString) {
  const date = new Date(dateString);
  return `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()}`;
}

function formatCommitsAsTable(commits) {
  // Exactly 1 latest commit per repository, sorted by date descending
  const repoList = Object.values(commits)
    .filter(c => c && c.repo && c.sha)
    .sort((a, b) => new Date(b.date) - new Date(a.date))
    .slice(0, 18); // Shows 18 distinct active repositories

  if (repoList.length === 0) return "";

  const rows = repoList.map(c => {
    const repoLink = `**[${c.repo}](https://github.com/${c.repo})**`;
    const commitLink = `[\`${c.sha.slice(0, 7)}\`](${c.url}) ${c.message}`;
    const when = `\`${formatDate(c.date)}\``;
    return `| ${repoLink} | ${commitLink} | ${when} |`;
  });

  return rows.join("\n");
}

async function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function fetchUserRepos() {
  try {
    const url = `https://api.github.com/users/${username}/repos?per_page=50&sort=pushed`;
    const { data } = await axios.get(url, { headers });
    if (Array.isArray(data)) {
      return data.map(r => r.full_name);
    }
  } catch (error) {
    console.error("   ⚠️  Could not fetch user repos:", error.message);
  }
  return [];
}

async function fetchEvents(page = 1) {
  const url = `https://api.github.com/users/${username}/events?page=${page}&per_page=100`;
  const { data } = await axios.get(url, { headers });
  return data;
}

async function fetchAllEvents() {
  console.log("📡 Fetching user events...");
  const events = [];
  for (let page = 1; page <= 5; page++) {
    try {
      const pageEvents = await fetchEvents(page);
      if (!pageEvents.length) break;
      events.push(...pageEvents);
      console.log(`   Fetched page ${page} (${pageEvents.length} events)`);
      await delay(100);
    } catch (error) {
      console.error(`   Error fetching page ${page}:`, error.message);
      break;
    }
  }
  console.log(`✅ Total events fetched: ${events.length}`);
  return events;
}

async function fetchLatestCommitForRepo(repo) {
  try {
    const url = `https://api.github.com/repos/${repo}/commits?per_page=1`;
    const { data } = await axios.get(url, { headers });
    if (data && Array.isArray(data) && data.length > 0) {
      const commit = data[0];
      return {
        repo,
        sha: commit.sha,
        message: commit.commit.message.split("\n")[0],
        date: commit.commit.author ? commit.commit.author.date : commit.commit.committer.date,
        url: commit.html_url
      };
    }
  } catch (error) {
    console.error(`   ⚠️  Could not fetch commits for ${repo}:`, error.message);
  }
  return null;
}

async function generateReadmeSection() {
  console.log("🚀 Starting single-commit-per-repo update...\n");

  const cache = loadCache();
  const repoSet = new Set();

  // Known organization & campus repos
  const defaultRepos = [
    "cscnitc/blog-site",
    "csea-nitc/venue-portal-backend",
    "csea-nitc/venue-portal-frontend",
    "IEEE-SB-NITC/ieee-sb-nitc"
  ];
  defaultRepos.forEach(r => repoSet.add(r));

  // 1. Fetch repositories from events
  const events = await fetchAllEvents();
  for (const event of events) {
    if (event.type === "PushEvent" && event.repo) {
      repoSet.add(event.repo.name);
    }
  }

  // 2. Fetch user's own recently pushed repos
  const userRepos = await fetchUserRepos();
  userRepos.forEach(r => repoSet.add(r));

  // 3. Include existing repos from cache
  Object.keys(cache).forEach(repo => repoSet.add(repo));

  console.log(`✅ Tracking ${repoSet.size} repositories...\n`);

  let updateCount = 0;
  for (const repo of repoSet) {
    try {
      const commitData = await fetchLatestCommitForRepo(repo);
      if (commitData) {
        if (!cache[repo] || new Date(commitData.date) >= new Date(cache[repo].date)) {
          cache[repo] = commitData;
          updateCount++;
          console.log(`   ✓ Updated: ${repo}`);
        }
      }
      await delay(120);
    } catch (error) {
      console.error(`   ✗ Error with ${repo}:`, error.message);
    }
  }

  console.log(`\n✅ Cache updated (${updateCount} repos refreshed)\n`);
  saveCache(cache);

  const tableRows = formatCommitsAsTable(cache);

  // Update README
  const readme = fs.readFileSync(readmePath, "utf8");
  const startMarker = "| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |";
  const endMarker = "<!--END_CONTRIBUTED_REPOS-->";

  const startIndex = readme.indexOf(startMarker);
  const endIndex = readme.indexOf(endMarker);

  if (startIndex !== -1 && endIndex !== -1) {
    const before = readme.substring(0, startIndex + startMarker.length);
    const after = readme.substring(endIndex);

    const newReadme = `${before}\n${tableRows}\n\n${after}`;
    fs.writeFileSync(readmePath, newReadme);
    console.log("✅ README updated successfully (1 commit per repository across all active repos)!");
  } else {
    console.error("❌ Could not find table markers in README.md");
  }
}

generateReadmeSection().catch(err => {
  console.error("❌ Failed:", err.message);
  console.error(err.stack);
});
