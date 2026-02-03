import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv("netflix.csv")

# Display dataset
print("Dataset Preview:")
print(data.dtypes)

# Movies vs TV Shows
type_count = data['type'].value_counts()
print("\nMovies vs TV Shows:")
print(type_count)

type_count.plot(kind='bar')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Country-wise content
country_count = data['country'].value_counts().head(10)

country_count.plot(kind='bar')
plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Shows")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Year-wise release
year_count = data['release_year'].value_counts().sort_index()
print("\nYear-wise Releases:")
print(year_count)

year_count.plot()
plt.title("Content Release Over Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# Rating-wise distribution
rating_count = data['rating'].value_counts().head(6)

rating_count.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Top Rating Distribution on Netflix")
plt.ylabel("")
plt.tight_layout()
plt.show()

plt.pie(
    
)
# ==============================
# Top 5 Popular Movies (Genre-based)
# ==============================

# 1. Filter only Movies
movies = data[data['type'] == 'Movie']

# 2. Extract main genre (first genre from listed_in)
movies['main_genre'] = movies['listed_in'].str.split(',').str[0]

# 3. Count genre popularity
genre_count = movies['main_genre'].value_counts()

print("\nTop 5 Popular Genres:")
print(genre_count.head(5))

# 4. Get top 5 genres
top_genres = genre_count.head(5).index

# 5. Get top 5 movies from popular genres
top5_movies = movies[movies['main_genre'].isin(top_genres)][
    ['title', 'main_genre', 'release_year']
].head(5)

print("\nTop 5 Most Popular Movies and Their Genres:")
print(top5_movies)

# 6. Bar graph for top genres
genre_count.head(5).plot(kind='bar')
plt.title("Top 5 Popular Movie Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.show()


#Abhsihek is this is wrong



