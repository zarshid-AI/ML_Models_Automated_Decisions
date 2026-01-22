import pandas as pd
from pathlib import Path

script_dir = Path(__file__).resolve().parent          
project_root = script_dir.parent

# Read the CSV files
github_domain_repos = pd.read_csv('./data/github_domain_repos.csv')
csv_path = './data/sorted_dependents_repo_huggingface_transformers.csv'
sorted_dependents = pd.read_csv(csv_path)

# Strip whitespace from column names and string columns
github_domain_repos.columns = github_domain_repos.columns.str.strip()
sorted_dependents.columns = sorted_dependents.columns.str.strip()

# Strip whitespace from the 'name' and 'dependent' columns
github_domain_repos['name'] = github_domain_repos['name'].str.strip()
sorted_dependents['dependent'] = sorted_dependents['dependent'].str.strip()

# Create a new dataframe to store the matched results
matched_data = []

# Iterate through github_domain_repos and check if 'name' matches any 'dependent'
for _, domain_row in github_domain_repos.iterrows():
    repo_name = domain_row['name']
    
    # Check if this repo name appears in the dependent column
    matches = sorted_dependents[sorted_dependents['dependent'] == '/' + repo_name]
    
    # If there are matches, add them to the result
    for _, dep_row in matches.iterrows():
        matched_record = {
            'stars': domain_row['stars'],
            'forks': domain_row['forks'],
            'domain': domain_row['domain'],
            'language': domain_row['language'],
            'repoName': dep_row['repoName'],
            'dependent': dep_row['dependent'],
            'sub-field': domain_row['sub-field'],
            'github_link': domain_row['github_link']
        }
        matched_data.append(matched_record)

# Create a dataframe from the matched data
result_df = pd.DataFrame(matched_data)

# Save to a new CSV file
output_filename = './data/matched_repos_with_dependent_before_checking_decision_making.csv'
result_df.to_csv(output_filename, index=False)

# print(f"Matching complete! Found {len(result_df)} matches.")
# print(f"Results saved to '{output_filename}'")
# print("\nFirst few rows of the result:")
# print(result_df.head())