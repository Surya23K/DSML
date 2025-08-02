import matplotlib.pyplot as plt

# Sample data
data = [12, 15, 13, 19, 21, 21, 22, 25, 25, 26, 28, 30, 31, 32, 34, 35, 35, 36, 37, 39, 40, 42, 44, 45, 46, 48, 50]

# Creating histogram
plt.hist(data, bins=10, color='skyblue', edgecolor='black')

# Adding titles and labels
plt.title('Histogram of Sample Data')
plt.xlabel('Value Range')
plt.ylabel('Frequency')

# Display the plot
plt.show()
