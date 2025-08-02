import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

# Load the dataset
diabetes_bunch = load_diabetes()
diabetes = pd.DataFrame(diabetes_bunch.data, columns=diabetes_bunch.feature_names)
diabetes['target'] = diabetes_bunch.target  # Disease progression

# Shape and basic info
print("Shape of dataset:", diabetes.shape)
print("\nFirst 5 rows:")
print(diabetes.head())

print("\nDatatypes and Non-Null Info:")
print(diabetes.info())

print("\nSummary Statistics:")
print(diabetes.describe())

print("\nMissing Values:")
print(diabetes.isnull().sum())

# Target variable distribution
print("\nTarget Variable (Progression) Description:")
print(diabetes['target'].describe())

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(diabetes.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix - Diabetes Dataset")
plt.show()

# Boxplot of features (excluding target)
plt.figure(figsize=(12, 6))
sns.boxplot(data=diabetes.drop('target', axis=1))
plt.title("Boxplot of Diabetes Features")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Pairplot with limited features (to avoid overload)
sns.pairplot(diabetes[['bmi', 'bp', 's1', 's5', 'target']])
plt.suptitle("Pairplot of Selected Diabetes Features", y=1.02)
plt.show()

