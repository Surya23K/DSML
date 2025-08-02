import matplotlib.pyplot as plt

# Sample data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
prices = [120, 125, 123, 130, 128, 135, 140]

# Plotting the price chart
plt.plot(days, prices, marker='o', linestyle='-', color='blue')

# Adding titles and labels
plt.title('Product Price Over the Week')
plt.xlabel('Day')
plt.ylabel('Price (₹)')
plt.grid(True)

# Display the chart
plt.show()
