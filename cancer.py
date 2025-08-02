import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

# Load the dataset
cancer_bunch = load_breast_cancer()
cancer = pd.DataFrame(cancer_bunch.data, columns=cancer_bunch.feature_names)
cancer['diagnosis'] = cancer_bunch.target
cancer['diagnosis'] = cancer['diagnosis'].map({0: 'malignant', 1: 'benign'})

# Shape and structure
print("Shape of dataset:", cancer.shape)
print("\nFirst 5 rows:")
print(cancer.head())

print("\nDatatypes and Non-Null Info:")
print(cancer.info())

print("\nSummary Statistics:")
print(cancer.describe())

print("\nMissing Values:")
print(cancer.isnull().sum())

print("\nClass Distribution:")
print(cancer['diagnosis'].value_counts())

# Pairplot on limited features to avoid overload
sns.pairplot(cancer[['mean radius', 'mean texture', 'mean area', 'mean smoothness', 'diagnosis']], hue='diagnosis')
plt.suptitle("Pairplot of Breast Cancer Features", y=1.02)
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(cancer.drop('diagnosis', axis=1).corr(), annot=False, cmap='coolwarm')
plt.title("Feature Correlation Matrix - Breast Cancer")
plt.show()

# Boxplot for selected features
plt.figure(figsize=(12, 6))
sns.boxplot(data=cancer.drop('diagnosis', axis=1)[['mean radius', 'mean texture', 'mean area', 'mean smoothness']])
plt.title("Boxplot for Selected Features - Breast Cancer")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()