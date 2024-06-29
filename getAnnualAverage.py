from collections import defaultdict
import random

# List of possible codes
codes = ["AA", "XA", "FC", "FD"]

# Generate 1000 entries with random years from 2013 to 2022
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

# Read data from file and count applications by year and code
annual_report = defaultdict(lambda: defaultdict(int))

with open(file_path, 'r') as file:
    for line in file:
        app_id, code, year = line.strip().split(',')
        annual_report[int(year)][code] += 1

# Write annual report to a file
report_file_path = 'data/annual_report.txt'
with open(report_file_path, 'w') as report_file:
    report_file.write("Year,AA,XA,FC,FD\n")
    for year in sorted(annual_report.keys()):
        line = f"{year},{annual_report[year]['AA']},{annual_report[year]['XA']},{annual_report[year]['FC']},{annual_report[year]['FD']}\n"
        report_file.write(line)

print(f"Annual report saved to {report_file_path}")
