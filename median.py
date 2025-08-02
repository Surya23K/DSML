import numpy as np
import matplotlib.pyplot as plt

# Sample dataset (you can change this to your own data)
data = [12, 15, 14, 10, 18, 20, 22, 25, 28, 30, 32, 35, 40]

# Calculate mean and median
mean_val = np.mean(data)
median_val = np.median(data)

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=8, color='skyblue', edgecolor='black', alpha=0.7)

# Plot mean and median lines
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {mean_val:.2f}')
plt.axvline(median_val, color='green', linestyle='dotted', linewidth=2, label=f'Median = {median_val:.2f}')

# Add labels and title
plt.title("Graphical Representation of Mean and Median")
plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
