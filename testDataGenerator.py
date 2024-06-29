import random

# List of possible codes
codes = ["AA", "XA", "FC", "FD"]

# Generate 1000 entries
num_entries = 1000
entries = []

# Generate random years from 2013 to 2022
years = list(range(2013, 2023))

for i in range(1, num_entries + 1):
    code = random.choice(codes)
    year = random.choice(years)
    entries.append(f"{i:03},{code},{year}")

# Write the entries to a file
file_path = 'data/applications_with_years.txt'
with open(file_path, 'w') as file:
    file.write("\n".join(entries))

print(f"{num_entries} entries with random years written to {file_path}")
