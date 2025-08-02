import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset from seaborn
titanic = sns.load_dataset('titanic')

# Show first 5 rows
print(titanic.head())

# Dataset info
print(titanic.info())

# Check for missing values
print(titanic.isnull().sum())

# Basic statistics
print(titanic.describe(include='all'))

# Survival counts
print(titanic['survived'].value_counts())

# Plot survival count
sns.countplot(x='survived', data=titanic)
plt.title('Survival Count')
plt.show()

# Survival rate by sex
sns.barplot(x='sex', y='survived', data=titanic)
plt.title('Survival Rate by Sex')
plt.show()

# Survival rate by passenger class (Pclass)
sns.barplot(x='pclass', y='survived', data=titanic)
plt.title('Survival Rate by Passenger Class')
plt.show()

# Age distribution by survival status
plt.figure(figsize=(10,6))
sns.kdeplot(titanic.loc[titanic['survived'] == 1, 'age'].dropna(), label='Survived', shade=True)
sns.kdeplot(titanic.loc[titanic['survived'] == 0, 'age'].dropna(), label='Did Not Survive', shade=True)
plt.title('Age Distribution by Survival Status')
plt.legend()
plt.show()
