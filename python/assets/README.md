
This folder contains CSV files that are used in the project for analysis and comparison of GitHub repositories based on domain and dependencies.

## Files

### github_domain_repos.csv
This file contains repositories fetched from GitHub based on specific domains or topics. The columns in this file are as follows:
- **repoName**: Name of the repository (owner name/project name).
- **stars**: Number of stars the repository has received, indicating its popularity.
- **forks**: Number of forks of the repository, showing how many users have copied the repository for their own use.
- **total_commits**: Number of total commits of the repositories.
- **last_commit_month**: Month of last commit
- **last_commit_author**: Author of last commit
- **language**: The primary programming language used in the repository.
- **github_link**: The URL to access the repository on GitHub.
- **domain**: The specific domain/topic under which the repository is categorized.
- **sub-field**: The specific sub-domain under which the domain is sub-categorized.

### matched_repos_with_dependent_before_checking_decision_making.csv
This file contains matched records of repositories before any decision filtering is applied. The columns in this file are as follows:
- **repoName**: Name of the repository (owner name/project name).
- **stars**: Number of stars the repository has received, indicating its popularity.
- **forks**: Number of forks of the repository, showing how many users have copied the repository for their own use.
- **total_commits**: Number of total commits of the repositories.
- **last_commit_month**: Month of last commit
- **last_commit_author**: Author of last commit
- **language**: The primary programming language used in the repository.
- **github_link**: The URL to access the repository on GitHub.
- **domain**: The specific domain/topic under which the repository is categorized.
- **sub-field**: The specific sub-domain under which the domain is sub-categorized.