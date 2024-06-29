from collections import Counter

# File paths
input_file_path = 'data/applications.txt'
output_file_path = 'data/totalAnnualUniqueApplications.txt'

# Function to load data from file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data

# Load data from file
data = load_data(input_file_path)

# Count occurrences of each application ID
id_counts = Counter()
for entry in data:
    app_id, product_code = entry.split(',')
    id_counts[app_id] += 1

# Write counts to output file
with open(output_file_path, 'w') as outfile:
    for app_id, count in id_counts.items():
        outfile.write(f"Application ID {app_id}: {count} occurrences\n")

print(f"Count of unique application IDs written to '{output_file_path}'.")
