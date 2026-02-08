import pandas as pd

print("📺 Netflix Data Analysis\n")

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns)

# Remove missing values
df = df.dropna(subset=["country", "rating"])

# Movies vs TV Shows
print("\nMovies vs TV Shows:")
print(df["type"].value_counts())

# Top countries
print("\nTop 5 Countries:")
print(df["country"].value_counts().head())

# Top ratings
print("\nTop Ratings:")
print(df["rating"].value_counts().head())

# Recent content
recent = df[df["release_year"] >= 2018]
print("\nContent released after 2018:", recent.shape[0])
