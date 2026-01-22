# Replication Package
This replication package contains the necessary data and Python script to for reproducing the results of our paper: "Machine Learning in the Wild: Early Evidence of Non-Compliant ML-Automation in Open-Source Software", aimed at examining the automated-decision process of high-risk open-source projects. 

## Project Structure
The project is organized as follows:

### ``data/``: Contains datasets used in the project
  - ``sorted_dependents_repo_huggingface_transformers.csv``: This file contains a pre-sorted list of dependents of the huggingface/transformer library on GitHub. For each client project the file reports: (i) name of the project, (ii) number of stars, and (iii) number of forks.
  - ``github_domain_repos.csv``: Repositories fetched by domain/topic from github have following feature about repository name, stars, forks, language, github link, last commit, last commit month, domain ans sub-domain name.
  - ``matched_repos_with_dependent_before_checking_decision_making.csv``: Matched records before decision filtering which have infomation about repository name, stars, forks, language, github link, last commit, last commit month, domain ans sub-domain name.

### ``python/``: Contains Python scripts and dependencies.
  - ``README.md``: Describes the contents of the python folder.
  - ``requirements.txt``: Lists the Python package dependencies required for the project.
  - ``.env``: Holds environment variables, including the GitHub token.
  - ``example.env``: Example environment file to copy and populate with your GitHub token.
  - ``domain_wise_repository_github.py``: python script queries GitHub by domain/topic and saves repository metadata.
  - ``compare_sorted_dependents_repo_huggingface_with_git_domain_wise_data.py``: Python script compares domain-fetched repositories with the HuggingFace dependents CSV and produces matched output.

### ``results/``: Contains output files from the analysis.
  - ``README.md``: Explains the contents of the results folder.
  - ``final_decision_making_repos.csv``:  This file contains the final list of selected GitHub repositories. Each row represents one project used in the decision-making analysis. It helps track which repositories are included and compared. The file is mainly for reference and evaluation.
  - ``github_systems_domain_wise_workflow.pdf``: extented work flow of github repository from input to output each step (input, pre-processing, decision, post-processing, output)
  - ``automated_decision_types.pdf``: Contains clustering outputs of github projects and their explanations.
  - ``postprocessing_rulebase_cluster.pdf``: Describes the rule-based postprocessing applied to clusters and selection logic.

### ``appendix/``: Contains additional analysis documents.
  - ``README.md``: Explains the contents of the appendix folder.
  - ``github_projects_domain_sub-domains_analysis.pdf``: Analysis of GitHub projects by domain and sub-domain.
  - ``output_categories.pdf``: Outlines the categories of outputs from the project.
  - ``unique_models_github_systems_analysis.pdf``: Analysis of unique models in GitHub systems.

## Setup Instructions

1. Ensure you have Python 3.8+ installed on your Windows machine.
2. Obtain a GitHub personal access token for higher API rate limits.
3. Install the required dependencies by running:
   ```
   pip install -r python/requirements.txt
   ```
4. Set up your environment by copying the example environment file and editing it to include your GitHub token:
   ```
   cd python
   copy example.env .env
   # Edit .env and set GITHUB_TOKEN=ghp_...
   ```
5. Ensure the required data files exist in the `data` folder.

## How to Run

- Fetch domain repositories:
   ```
   cd python
   python domain_wise_repository_github.py
   ```
- Compare fetched domain repos with the pre-sorted dependents CSV:
   ```
   python compare_sorted_dependents_repo_huggingface_with_git_domain_wise_data.py
   ```
