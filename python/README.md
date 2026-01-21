This file provides an overview of the contents of the `python` folder within the ML Models Automated Decisions project. It includes details about the required dependencies, scripts, and their functionalities.

## Folder Structure

- **requirements.txt**: This file lists the Python package dependencies required for the project. Ensure to install these packages to run the scripts successfully.

- **assets/**: This subfolder contains CSV files that are used for data processing and analysis.
  - **README.md**: This file explains the contents of the assets folder, detailing the purpose of the CSV files contained within.
  - **github_domain_repos.csv**: This file contains repositories fetched by domain/topic. **matched_repos_with_dependent_before_checking_decision_making.csv**: This file contains matched records before decision filtering. 

- **script/**: This subfolder contains the main scripts for querying and comparing repositories.
  - **README.md**: This file describes the scripts in the script folder, detailing the functionality of each script.
  - **.env**: This file holds environment variables, including the GitHub token, and is not committed to version control.
  - **example.env**: This file is an example environment file to copy and populate with your GitHub token.
  - **domain_wise_repository_github.py**: This script queries GitHub by domain/topic and saves repository metadata.
  - **compare_sorted_dependents_repo_huggingface_with_git_domain_wise_data.py**: This script compares domain-fetched repositories with the HuggingFace dependents CSV and produces matched output.
