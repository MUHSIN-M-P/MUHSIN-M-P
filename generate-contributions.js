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

function formatDate(dateString) {
  const date = new Date(dateString);
  return `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()}`;
}

function formatCommitsAsTable(commits) {
  // Sort by date and take top 10
  const topCommits = Object.values(commits)
    .sort((a, b) => new Date(b.date) - new Date(a.date))
    .slice(0, 10);

  if (topCommits.length === 0) return "";

  const rows = topCommits.map(c => {
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

async function fetchEvents(page = 1) {
  const url = `https://api.github.com/users/${username}/events?page=${page}&per_page=100`;
  const { data } = await axios.get(url, { headers });
  return data;
}

async function fetchAllEvents() {
  console.log("📡 Fetching user events...");
  const events = [];
  for (let page = 1; page <= 10; page++) {
    try {
      const pageEvents = await fetchEvents(page);
      if (!pageEvents.length) break;
      events.push(...pageEvents);
      console.log(`   Fetched page ${page} (${pageEvents.length} events)`);
      await delay(100); // Rate limiting
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
    if (data && data.length > 0) {
      const commit = data[0];
      return {
        repo,
        sha: commit.sha,
        message: commit.commit.message.split('\n')[0], // First line only
        date: commit.commit.author.date,
        url: commit.html_url
      };
    }
  } catch (error) {
    console.error(`   ⚠️  Could not fetch commits for ${repo}:`, error.message);
  }
  return null;
}

async function generateReadmeSection() {
  console.log("🚀 Starting contribution update...\n");
  
  const cache = loadCache();
  const events = await fetchAllEvents();
  const repoSet = new Set();

  // Extract all repos from push events
  console.log("\n📦 Extracting repositories from events...");
  for (const event of events) {
    if (event.type === "PushEvent") {
      repoSet.add(event.repo.name);
    }
  }
  console.log(`✅ Found ${repoSet.size} repositories with push events\n`);

  // Also include repos already in cache
  Object.keys(cache).forEach(repo => repoSet.add(repo));

  // Update cache with latest commits from each repo
  console.log("🔄 Fetching latest commits for all repositories...");
  let updateCount = 0;
  
  for (const repo of repoSet) {
    try {
      const commitData = await fetchLatestCommitForRepo(repo);
      
      if (commitData) {
        // Update cache if this is a new repo or has a newer commit
        if (!cache[repo] || new Date(commitData.date) > new Date(cache[repo].date)) {
          cache[repo] = commitData;
          updateCount++;
          console.log(`   ✓ Updated: ${repo}`);
        } else {
          console.log(`   - No change: ${repo}`);
        }
      }
      
      await delay(150); // Rate limiting
    } catch (error) {
      console.error(`   ✗ Error with ${repo}:`, error.message);
    }
  }

  console.log(`\n✅ Updated ${updateCount} repositories\n`);

  // Save updated cache
  saveCache(cache);
  console.log("💾 Cache saved\n");

  // Generate table format
  const tableRows = formatCommitsAsTable(cache);
  
  // Read and update README
  const readme = fs.readFileSync(readmePath, "utf8");
  
  // Find the table section and replace it
  const startMarker = "| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |";
  const endMarker = "<!--END_CONTRIBUTED_REPOS-->";
  
  const startIndex = readme.indexOf(startMarker);
  const endIndex = readme.indexOf(endMarker);
  
  if (startIndex !== -1 && endIndex !== -1) {
    const before = readme.substring(0, startIndex + startMarker.length);
    const after = readme.substring(endIndex);
    
    const newReadme = `${before}\n${tableRows}\n\n${after}`;
    fs.writeFileSync(readmePath, newReadme);
    console.log("✅ README updated successfully!");
    console.log(`📊 Showing top 10 most recent commits from ${Object.keys(cache).length} total repositories\n`);
  } else {
    console.error("❌ Could not find table markers in README.md");
  }
}

generateReadmeSection().catch(err => {
  console.error("❌ Failed:", err.message);
  console.error(err.stack);
});
