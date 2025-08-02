import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate random values (e.g., 100 numbers between 10 and 100)
np.random.seed(42)  # For consistent results
data = np.random.randint(10, 100, size=100)

# Step 2: Calculate mean and median
mean_val = np.mean(data)
median_val = np.median(data)

# Step 3: Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=10, color='lightblue', edgecolor='black', alpha=0.7)

# Plot mean and median lines
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {mean_val:.2f}')
plt.axvline(median_val, color='green', linestyle='dotted', linewidth=2, label=f'Median = {median_val:.2f}')

# Step 4: Add labels and title
plt.title("Random Data with Mean and Median")
plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)

# Step 5: Display the plot
plt.show()

# Step 6: Print values (optional)
print("Generated Data (first 20 values):", data[:20])
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
