import matplotlib.pyplot as plt

# Sample data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# Creating the scatter plot
plt.scatter(x, y, color='green', marker='o')

# Adding titles and labels
plt.title('Scatter Diagram Example')
plt.xlabel('X-axis values')
plt.ylabel('Y-axis values')

# Display the plot
plt.show()
