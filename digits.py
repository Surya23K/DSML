
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# Load dataset
digits_bunch = load_digits()

# Data and target
X = digits_bunch.data  # shape (1797, 64)
y = digits_bunch.target

# Convert to DataFrame
digits = pd.DataFrame(X, columns=[f'pixel_{i}' for i in range(X.shape[1])])
digits['target'] = y

# Dataset shape and type info
print("Shape of dataset:", digits.shape)
print("\nTarget classes:", np.unique(y))

# Check for missing values
print("\nMissing values per column:")
print(digits.isnull().sum())

# Class distribution
print("\nClass distribution:")
print(digits['target'].value_counts().sort_index())

# Plot some sample images
fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X[i].reshape(8, 8), cmap='gray')
    ax.set_title(f"Label: {y[i]}")
    ax.axis('off')
plt.suptitle("Sample Digits from Dataset")
plt.tight_layout()
plt.show()

# Correlation heatmap of first 20 pixels (to reduce clutter)
plt.figure(figsize=(10, 6))
sns.heatmap(digits.iloc[:, :20].corr(), cmap="coolwarm", annot=False)
plt.title("Correlation Between First 20 Pixels")
plt.show()

# Boxplot of pixel values for a few pixels
plt.figure(figsize=(12, 6))
sns.boxplot(data=digits[[f'pixel_{i}' for i in range(10)]])
plt.title("Boxplots of First 10 Pixel Features")
plt.show()
