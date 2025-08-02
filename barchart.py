import matplotlib.pyplot as plt

# Sample data
categories = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
values = [23, 17, 35, 29, 12]

# Creating the bar chart
plt.bar(categories, values, color='orange', edgecolor='black')

# Adding titles and labels
plt.title('Fruit Sales Bar Chart')
plt.xlabel('Fruits')
plt.ylabel('Quantity Sold')

# Display the plot
plt.show()
