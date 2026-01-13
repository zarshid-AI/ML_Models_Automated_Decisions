Prerequisites
- Python 3.8+
- Windows machine (commands shown below)
- A GitHub personal access token for higher API rate limits

Install dependencies
Open PowerShell or Command Prompt at the project root and run:
```
pip install -r python/requirements.txt
```

Setup
1. Copy the example env and set your GitHub token:
```
cd python\script
copy example.env .env
# Edit .env and set GITHUB_TOKEN=ghp_...
```
2. Ensure required data files exist in the data and python/assets folders.

How to run
- Fetch domain repositories (queries GitHub; requires .env with token):
```
cd python\script
python domain_wise_repository_github.py
```
- Compare fetched domain repos with the pre-sorted dependents CSV:
```
python compare_sorted_dependents_repo_huggingface_with_git_domain_wise_data.py
```

Project structure and one-line description for every file

Root
- README.md — This file: overview, setup and file-level descriptions.
- ML_decisonmaking_research_project.png — This image: overview, number project analyised and final decision making projects.
- github_projects_domain_sub-domains_analysis.pdf — This pdf: domain and sub-domain analysis of github projects.

data
- sorted_dependents_repo_huggingface_transformers.csv — Pre-sorted list of dependents of HuggingFace Transformers used to match against domain repos.

python
- requirements.txt — Python package dependencies required by the scripts.

python/assets
- github_domain_repos.csv — CSV of repositories fetched by domain/topic (expected input for compare script).
- matched_repos_with_dependent_before_checking_decision_making.csv — Output of the compare script containing matched records before decision filtering.

python/script
- .env — Environment file holding secrets (GitHub token); not committed to VCS and used by domain fetch script.
- example.env — Example env file to copy and populate with your GitHub token.
- domain_wise_repository_github.py — Script to query GitHub by domain/topic and save repository metadata (name, stars, forks, language, link, domain).
- compare_sorted_dependents_repo_huggingface_with_git_domain_wise_data.py — Script to compare domain-fetched repos with the HuggingFace dependents CSV and produce matched output.


results
- final_decision_making_repos.csv — Post-processed CSV of repositories selected after decision-making or manual review.
- github_model_domain_wise.docx — Word document summarizing model/domain-wise repository selections and notes.
- output_clusters.docx — Word document containing clustering outputs, visualizations, and explanations.
- postprocessing_rulebase_cluster.docx — Documentation of rule-based postprocessing applied to clusters and selection logic.

Notes & troubleshooting
- Ensure CSV encodings are UTF-8 to avoid pandas read errors.
- The compare script expects consistent column names (e.g., repository name fields); mismatches will prevent correct matching.
- GitHub API rate limits apply; include a valid token in python/script/.env to increase query limits.
- If domain fetch writes output to a different path, move that CSV to python/assets/github_domain_repos.csv for the compare script to find it.

Contributing
- Modify search domains or topics inside python/script/domain_wise_repository_github.py to change which repositories are collected.
- Adjust matching logic or output columns inside python/script/compare_sorted_dependents_repo_huggingface_with_git_domain_wise_data.py.
