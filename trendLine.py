import numpy as np
import matplotlib.pyplot as plt

# Read data from the .txt file
file_path = 'annualAverageApplicants.txt'
with open(file_path, 'r') as file:
    data = file.readlines()

# Convert data to a list of integers
data = [int(line.strip()) for line in data]

# Generate x values (years or any time indicator)
x = np.arange(1, len(data) + 1)

# Convert data to a numpy array
y = np.array(data, dtype=np.float64)

# Fit a polynomial of degree 1 (linear trend)
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)

# Calculate the trendline values
trendline = polynomial(x)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data')
plt.plot(x, trendline, 'r--', label='Trendline')

# Labels and title
plt.xlabel('Time')
plt.ylabel('Number of Applicants')
plt.title('Trendline of Annual Applicants')
plt.legend()

# Show the plot
plt.show()
