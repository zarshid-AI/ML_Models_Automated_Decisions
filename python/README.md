This file provides an overview of the contents of the `python` folder within the ML Models Automated Decisions project. It includes details about the required dependencies, scripts, their functionalities, and environment configuration files necessary for querying GitHub repositories by domain and comparing them with HuggingFace Transformers dependents.

1. **domain_wise_repository_github.py**
   - This script queries GitHub for repositories based on specified domains or topics. It retrieves metadata for each repository, including: repository_name, stars, forks, language, link, domain, sub-domain. 

2. **compare_sorted_dependents_repo_huggingface_with_git_domain_wise_data.py**
   - This script compares the repositories fetched by the domain-wise query with the pre-sorted list of dependents of HuggingFace Transformers of Github projects. It produces an output of matched records before any decision filtering.

### Environment Files

1. **.env**
   - This file holds environment variables, including the GitHub personal access token. It is not committed to version control to keep sensitive information secure.

2. **example.env**
   - This is an example environment file that users can copy and populate with their GitHub token for use in the project.

### Dependencies

1.  **requirements.txt**: This file lists the Python package dependencies required for the project. Ensure to install these packages to run the scripts successfully.


