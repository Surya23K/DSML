import matplotlib.pyplot as plt

# Sample data
x = [10, 20, 30, 40, 50]
y = [15, 25, 35, 45, 55]
bubble_size = [50, 300, 500, 700, 1000]  # Size of bubbles

# Creating the bubble chart
plt.scatter(x, y, s=bubble_size, color='red', alpha=0.5, edgecolors='orange')

# Adding titles and labels
plt.title('Bubble Chart Example')
plt.xlabel('X-axis values')
plt.ylabel('Y-axis values')

# Show the plot
plt.show()
