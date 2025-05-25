const fs = require("fs");
const axios = require("axios");
require("dotenv").config();
const username = "MUHSIN-M-P"; // ✅ Replace with your GitHub username
const token = process.env.GITHUB_TOKEN; // ✅ Use GitHub Personal Access Token from environment variable

if (!token) {
  throw new Error("GITHUB_TOKEN environment variable is not set.");
}

const headers = {
  Authorization: `token ${token}`,
  "User-Agent": "GitHub-Contrib-Script"
};

async function getRepos() {
  const url = `https://api.github.com/users/${username}/repos?per_page=100`;
  const { data } = await axios.get(url, { headers });
  return data.map(repo => ({
    name: repo.name,
    full_name: repo.full_name,
    fork: repo.fork
  }));
}

async function getBranches(full_name) {
  const url = `https://api.github.com/repos/${full_name}/branches`;
  const { data } = await axios.get(url, { headers });
  return data.map(b => b.name);
}

async function getCommits(full_name, branch) {
  const url = `https://api.github.com/repos/${full_name}/commits?sha=${branch}&per_page=5`;
  const { data } = await axios.get(url, { headers });
  return data.map(commit => ({
    message: commit.commit.message,
    date: commit.commit.author.date,
    url: commit.html_url,
    repo: full_name,
    branch
  }));
}

function formatCommits(commits) {
  return commits
    .map(
      c =>
        `- [${c.repo} \`${c.branch}\`](${c.url}): ${c.message} (${new Date(c.date).toLocaleDateString()})`
    )
    .join("\n");
}

async function generateReadmeSection() {
  const repos = await getRepos();
  const allCommits = [];

  for (const repo of repos) {
    const branches = await getBranches(repo.full_name);
    for (const branch of branches) {
      const commits = await getCommits(repo.full_name, branch);
      allCommits.push(...commits);
    }
  }

  const content = `<!--START_CUSTOM_COMMITS-->\n## 📝 Recent Commits\n${formatCommits(
    allCommits
  )}\n<!--END_CUSTOM_COMMITS-->`;

  const readmePath = "README.md";
  let readme = fs.readFileSync(readmePath, "utf8");

  const newReadme = readme.replace(
    /<!--START_CUSTOM_COMMITS-->[\s\S]*<!--END_CUSTOM_COMMITS-->/,
    content
  );

  fs.writeFileSync(readmePath, newReadme);
  console.log("✅ README updated with recent commits.");
}

generateReadmeSection().catch(err => {
  console.error("❌ Failed:", err.message);
});
