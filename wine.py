import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Load the wine dataset
wine_bunch = load_wine()

# Convert to DataFrame
wine = pd.DataFrame(wine_bunch.data, columns=wine_bunch.feature_names)
wine['target'] = wine_bunch.target
wine['target'] = wine['target'].map(dict(enumerate(wine_bunch.target_names)))

# Basic Exploration
print("Shape of dataset:", wine.shape)
print("\nFirst 5 rows:")
print(wine.head())

print("\nDatatypes and Non-Null counts:")
print(wine.info())

print("\nSummary Statistics:")
print(wine.describe())

print("\nMissing values per column:")
print(wine.isnull().sum())

print("\nClass Distribution:")
print(wine['target'].value_counts())

# Pairplot (optional: use only a few features if too many)
sns.pairplot(wine.iloc[:, :5].join(wine['target']), hue='target', diag_kind='kde')
plt.suptitle("Pairplot of Selected Wine Features", y=1.02)
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(wine.drop('target', axis=1).corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Wine Feature Correlation Matrix")
plt.show()

# Boxplot
plt.figure(figsize=(14, 6))
sns.boxplot(data=wine.drop('target', axis=1))
plt.title("Boxplot for Wine Features")
plt.xticks(rotation=90)
plt.show()
