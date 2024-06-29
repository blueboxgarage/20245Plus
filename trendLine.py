import matplotlib.pyplot as plt
import pandas as pd

# Path to annual report file
report_file_path = 'data/annual_report.txt'

# Load annual report data into a pandas DataFrame
df = pd.read_csv(report_file_path)

# Plotting
plt.figure(figsize=(10, 6))

# Plot trendlines for each product code
for code in ['AA', 'XA', 'FC', 'FD']:
    plt.plot(df['Year'], df[code], marker='o', label=code)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of Applications')
plt.title('Trend of Applications Received by Product Code')

# Add legend
plt.legend()

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()
