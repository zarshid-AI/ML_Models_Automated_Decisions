# Replication Package
This replication package contains the necessary data and Python script for reproducing the results of our paper: "Machine Learning in the Wild: Early Evidence of Non-Compliant ML-Automation in Open-Source Software".
The goal of the study is to analyze automated decision-making processes in open-source, high-risk ML projects.
It involves gathering data from GitHub, comparing it to the dependents of *huggingface/transformers*, manually reviewing the project's workflow, and clustering the post-processing and outputs of various projects.

## Project Structure

The project is organized into the following main directories and files:
### ``data/``: Contains datasets used in the project
  - ``sorted_dependents_repo_huggingface_transformers.csv``: This file contains a pre-sorted list of dependents of the huggingface/transformer library on GitHub. For each client project the file reports: (i) name of the project, (ii) number of stars, and (iii) number of forks.
  - ``github_domain_repos.csv``: This file contains the set of projects we have retrieved by searching by topics (application areas) using the GitHub API. For each project we report:
    - **repoName**: Name of the repository (owner name/project name).
    - **stars**: Number of stars.
    - **forks**: Number of forks.
    - **total_commits**: Number of total commits.
    - **last_commit_month**: Month of last commit.
    - **last_commit_author**: Author of last commit.
    - **last_commit_message**: Commit message of the last commit.
    - **language**: The primary programming language used in the repository.
    - **github_link**: The URL to access the repository on GitHub.
    - **domain**: The specific domain/topic under which the repository is categorized.
    - **sub-field**: The specific sub-domain under which the domain is sub-categorized.
  - ``matched_repos_with_dependent_before_checking_decision_making.csv``: This file is the result of the intersection between the high risk projects (``github_domain_repos.csv``) and the client projects importing the huggingface/transformer library (``sorted_dependents_repo_huggingface_transformers.csv``). It lists the initial sample accounting for 173 projects used to answer our research questions. 

### ``python/``: Contains Python scripts and dependencies.
  - ``requirements.txt``: Lists the Python package dependencies required for the project.
  - ``.env``: Holds environment variables, including the GitHub token.
  - ``example.env``: Example environment file to copy and populate with your GitHub token.
  - ``domain_wise_repository_github.py``: Python script queries GitHub by domain/topic and saves repository metadata.
  - ``compare_sorted_dependents_repo_huggingface_with_git_domain_wise_data.py``: Python script compares domain-fetched repositories with the HuggingFace dependents CSV and produces matched output.

### ``results/``: Contains output files from the analysis.
  - ``github_systems_domain_wise_workflow.pdf``: Extended workflow of a GitHub repository from input to output: each step includes input, pre-processing, decision, post-processing, and output.
  - ``automated_decision_types.pdf``: Contains clustering outputs of GitHub projects and their explanations.
  - ``postprocessing_rulebase_cluster.pdf``: Describes the rule-based post-processing applied to clusters and selection logic.
  - ``final_decision_making_repos.csv``:  This file contains the final list of selected GitHub repositories. Each row represents one project used in the decision-making analysis.
      - **domain**: Main application area of the project (such as healthcare or finance).
      - **repoName**: Short name of the GitHub repository.
      - **dependent**: Shows whether the project depends on other tools, models, or systems.
      - **sub-field**: Specific area within the main domain.
      - **repository_name**: Full or official name of the repository.
      - **domain_name**: standardized name of the project domain.
      - **sub_domain_name**:  standardized name of the project sub-domain.
      - **decision_type**: Type of decision the system performs 
      - **Traditional_ML_Model/ Logical**: Indicates use of traditional machine learning or rule-based logic.
      - **Transformer/Deep_Learning_Model**: Shows whether deep learning or transformer models are used.
      - **LLM_Used**: Name of the large language model used in the project, if any.
      - **model_output_usage**: How the model’s output is used to make final decisions.
      - **post-processing_type**: Type of rules or logic applied after the model output.
      - **cluster** : Cluster group assigned to the project based on its functionality.
      - **automation_level** : Level of automation (manual, semi-automatic, or fully automatic).
      - **term_of_use_restricted(yes/no)** : Indicates whether the repository has usage or violation of term of use.
      - **models** : List of AI or ML models used in the project.
    
### ``appendix/``: Contains additional analysis documents.
  - ``github_projects_domain_sub-domains_analysis.pdf``: Contains a table that illustrates the relationship between the main domains and their corresponding sub-domains.
  - ``output_categories.pdf``: This table summarizes the output-based categorization used in our study to classify GitHub projects that employ machine learning models for automated or semi-automated decision-making.
      - **Category Name**: the label used in the study to identify a class of decision outputs;
      - **Keywords**: representative terms observed in documentation or code that signal the presence of this output type;
      - **Description**: a concise explanation of the kind of decision or artifact generated by projects in this category.
  - ``unique_models_github_systems_analysis.pdf``: This table lists the unique machine learning models identified across the analyzed GitHub repositories and reports how often each model appears as a dependency. For each model, we show the repositories in which it is used and the corresponding usage count.

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