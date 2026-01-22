The `results` folder contains the output files generated from the project, summarizing the findings and decisions made during the analysis of GitHub repositories. Below is a description of each file contained within this folder:

### final_decision_making_repos.csv
- **stars**: Number of stars the repository has on GitHub.
- **forks**: Number of times the repository was forked by other users.

- **domain**: Main application area of the project (such as healthcare or finance).
- **language**: Primary programming language used in the project.
- **repoName**: Short name of the GitHub repository.
- **dependent**: Shows whether the project depends on other tools, models, or systems.
- **sub-field**: Specific area within the main domain.
- **github_link**: Direct link to the GitHub repository.
- **total_commits**: Total number of commits made to the repository.
- **last_commit_month**: Month when the last update was made to the repository.
- **last_commit_author**: Name of the person who made the most recent commit.
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


### github_systems_domain_wise_workflow.pdf
This file groups GitHub projects by their application domain. It shows which models belong to areas like healthcare, finance, driving, or security. The goal is to understand how AI models are spread across domains. It aids in domain-wise analysis and comparison.

### automated_decision_types.pdf
This file explains how output of projects are grouped into different clusters. Each cluster represents a type of task, such as control, vision, security, or advice. It also lists the projects that belong to each cluster. The document helps understand high-level project categorization.

### postprocessing_rulebase_cluster.pdf
This file describes rule-based methods used after AI model outputs. It explains different rule types like threshold checks, validation, and multi-agent voting. Each section includes simple examples from real projects. The file shows how rules improve safety, structure, and decision quality.