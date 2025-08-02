import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the OWID CSV data
df = pd.read_csv("suicide-rate-who-mdb.csv")  # assume it's been downloaded
# Display sample, info
print(df.head())
print(df.info())

# Filter for recent year, e.g. 2022
df2022 = df[df['year'] == 2022]

# Top and bottom 10 countries by rate
print("10 highest suicide rates in 2022")
print(df2022.nlargest(10, 'suicide_rate_per_100k')[['country', 'suicide_rate_per_100k']])
print("10 lowest")
print(df2022.nsmallest(10, 'suicide_rate_per_100k')[['country', 'suicide_rate_per_100k']])

# Trend of global average over time
global_trend = df.groupby('year')['suicide_rate_per_100k'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=global_trend, x='year', y='suicide_rate_per_100k')
plt.title("Global Average Suicide Rate (Age‑standardized, per 100k)")
plt.show()

# Country trends sample
sample_countries = ['India', 'United States', 'Japan', 'Russia']
plt.figure(figsize=(10, 6))
sns.lineplot(data=df[df['country'].isin(sample_countries)],
             x='year', y='suicide_rate_per_100k', hue='country')
plt.title("Suicide Rate Over Time by Country")
plt.legend()
plt.show()
