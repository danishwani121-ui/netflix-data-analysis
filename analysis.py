# ===============================
# 📺 Netflix Data Analysis Project
# ===============================

import pandas as pd
import matplotlib.pyplot as plt

print("📺 Netflix Data Analysis\n")

# --------------------------------
# 1️⃣ Load Dataset
# --------------------------------
df = pd.read_csv("netflix_titles.csv")

print("Dataset shape:", df.shape)
print("\nColumns in dataset:")
print(df.columns)

# --------------------------------
# 2️⃣ Data Cleaning
# --------------------------------
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove rows with missing country or rating
df = df.dropna(subset=["country", "rating"])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# --------------------------------
# 3️⃣ Movies vs TV Shows
# --------------------------------
type_counts = df["type"].value_counts()

print("\nMovies vs TV Shows:")
print(type_counts)

plt.figure()
type_counts.plot(kind="bar")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# --------------------------------
# 4️⃣ Top 10 Countries Producing Content
# --------------------------------
top_countries = df["country"].value_counts().head(10)

print("\nTop 10 Countries:")
print(top_countries)

plt.figure()
top_countries.plot(kind="bar")
plt.title("Top Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()

# --------------------------------
# 5️⃣ Most Common Ratings
# --------------------------------
top_ratings = df["rating"].value_counts().head(10)

print("\nTop Ratings:")
print(top_ratings)

plt.figure()
top_ratings.plot(kind="bar")
plt.title("Most Common Netflix Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# --------------------------------
# 6️⃣ Content Growth Over Years
# --------------------------------
year_data = df["release_year"].value_counts().sort_index()

plt.figure()
year_data.plot()
plt.title("Netflix Content Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

# --------------------------------
# 7️⃣ Content Released After 2018
# --------------------------------
recent = df[df["release_year"] >= 2018]
print("\nContent released after 2018:", recent.shape[0])

# --------------------------------
# 8️⃣ Extra Insight — Top Genres
# --------------------------------
# Split genres (listed_in column contains multiple genres)
genres = df["listed_in"].str.split(", ", expand=True).stack()
top_genres = genres.value_counts().head(10)

print("\nTop Genres on Netflix:")
print(top_genres)

plt.figure()
top_genres.plot(kind="bar")
plt.title("Top Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

print("\n✅ Analysis Completed Successfully!")
