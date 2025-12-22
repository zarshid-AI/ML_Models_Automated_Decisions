import csv
from dotenv import load_dotenv
from github import Github
import time
import os

token = os.getenv("GITHUB_TOKEN")
if not token:
    raise RuntimeError("GITHUB_TOKEN not found in environment. Add it to a .env file or export it.")

g = Github(token)

# Define domains and their related topics (sub-fields)
domains = {
    "healthcare": ["healthcare", "healthcare-ai", "healthcare-application", "healthcare-analysis", "healthcare-analytics", "ai-healthcare"],
    "banking": ["banking", "banking-applications", "banking-system", "bank-management-system", "open-banking"],
    "finance": ["finance", "fintech", "quantitative-finance", "financial-analysis", "finance-management", "yahoo-finance" ,"financial-analytics", "personal-finance"],
    "agriculture": ["agriculture", "smart-farming", "agricultural-modelling", "smart-agriculture", "precision-agriculture", "agricultural", "agriculture-research"],
    "drones": ["drones", "drone", "fpv-drones", "autonomous-drones", "droneswarm"],
    "autonomous-driving": ["autonomous-driving", "autonomous-vehicles", "self-driving-car", "end-to-end-autonomous-driving"],
    "automotive": ["automotive", "automotive-industry", "automotive-software", "automotive-security", "automotive-software", "automotive-applications"],
    "cybersecurity": ["cybersecurity", "cybersecurity-tools", "cybersecurity-projects", "cybersecurity-awareness", "cybersecurity-projects"],
    "blockchain": ["blockchain", "blockchain-technology", "blockchain-projects", "blockchain-game", "ethereum-blockchain", "blockchain-tool"],
    "energy": ["energy", "renewable-energy", "energy-efficiency", "energy-system", "solar-energy", "energy-production"],
    "transportation": ["transportation", "public-transport", "public-transportation", "transportation-management", "intelligent-transportation-systems", "transportation-planning"],
    "telecommunications": ["telecommunications", "telecommunication", "telecommunication-systems"],
    "smart-city": ["smart-city", "smart-cities", "smartcity", "smartcities"],
    "automated-hiring": ["hiring", "recruitment", "hiring-platform", "hiring-solutions", "hiring-challenge"],
    "dynamic-pricing": ["dynamic-pricing", "price-optimization", "dynamic-pricing-algorithm"],
    "compliance-checking-legal": ["compliance", "license-compliance", "compliance-automation", "gdpr-compliance", "compliance-check"]
}

# Language to filter (set to None for no language filter)
target_language = "python"

# Collect unique repos to avoid duplicates
seen_repos = set()
data = []

for domain, topics in domains.items():
    for topic in topics:
        # Build query: topic + optional language filter
        query = f"topic:{topic}"
        if target_language:
            query += f" language:{target_language}"

        try:
            repos = g.search_repositories(query=query, sort="stars", order="desc")
            for i, repo in enumerate(repos[:100000]):  # Top repos per topic
                repo_id = repo.full_name
                if repo_id in seen_repos:
                    continue  # Skip duplicates
                seen_repos.add(repo_id)

                # Get dependents count
                try:
                    dependents = repo.get_dependents().totalCount
                except:
                    dependents = 0

                # Get commit details
                try:
                    # Get default branch
                    default_branch = repo.default_branch

                    # Get commits from default branch
                    commits = repo.get_commits(sha=default_branch)

                    # Total commit count (this can be slow for large repos)
                    total_commits = commits.totalCount

                    # Get the latest commit
                    latest_commit = commits[0]
                    last_commit_date = latest_commit.commit.author.date
                    last_commit_message = latest_commit.commit.message
                    last_commit_author = latest_commit.commit.author.name

                except Exception as e:
                    print(f"Error getting commits for {repo.full_name}: {e}")
                    total_commits = 0
                    last_commit_date = "N/A"
                    last_commit_message = "N/A"
                    last_commit_author = "N/A"

                data.append({
                    "repoName": repo.full_name,
                    "dependent": dependents,
                    "stars": repo.stargazers_count,
                    "forks": repo.forks_count,
                    "total_commits": total_commits,
                    "last_commit_date": last_commit_date,
                    "last_commit_author": last_commit_author,
                    "last_commit_message": last_commit_message[:100] if last_commit_message != "N/A" else "N/A",  # Truncate message
                    "domain": domain,
                    "sub-field": topic,
                    "github_link": repo.html_url,
                    "language": target_language or repo.language or "N/A"
                })

                print(f"Processed: {repo.full_name} ({total_commits} commits)")

        except Exception as e:
            print(f"Error searching topic '{topic}': {e}")
            time.sleep(2)  # Pause to avoid rate limits

        # Respect rate limits
        time.sleep(0.5)

# Save to CSV
with open("github_domain_repos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "repoName", "dependent", "stars", "forks", "total_commits",
        "last_commit_date", "last_commit_author", "last_commit_message",
        "domain", "sub-field", "github_link", "language"
    ])
    writer.writeheader()
    writer.writerows(data)

print(f"Data saved to github_domain_repos.csv ({len(data)} unique repositories)")