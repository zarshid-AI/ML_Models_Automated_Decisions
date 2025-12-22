import pandas as pd

# Read the CSV file
input_file = "./data/research_paper_repos_dataset_selected.csv"
df = pd.read_csv(input_file)

# Convert Language column to lowercase
df["Language"] = df["Language"].str.lower()

# Filter rows where Language is 'python'
df_python = df[df["Language"] == "python"]

# Save to a new CSV file
output_file = "assest/research_paper_dataset_selected_python_only.csv"
df_python.to_csv(output_file, index=False)

print(f"Saved {len(df_python)} rows to '{output_file}'")
