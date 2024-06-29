import matplotlib.pyplot as plt

# Read data from the text file
file_path = 'data/topWNC.txt'
codes = []
counts = []

with open(file_path, 'r') as file:
    for line in file:
        code, count = line.strip().split(',')
        codes.append(code)
        counts.append(int(count))

# Generate a pie chart
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=codes, autopct='%1.1f%%', startangle=140)
plt.title('Average Count of Codes in the Last Year')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Save the pie chart as an image file
plt.savefig('pie_chart.png')

# Show the pie chart
plt.show()
