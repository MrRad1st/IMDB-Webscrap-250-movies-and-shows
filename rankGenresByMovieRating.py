import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_movie_dataset.xlsx' with the actual path to your Excel file
excel_path = 'your_movie_dataset.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_path)

# Calculate weighted scores for each genre
genre_ratings = {}

for index, row in df.iterrows():
    genres = row['genres'].split(', ')
    rating = row['popularity_rating']
    
    for genre in genres:
        if genre in genre_ratings:
            genre_ratings[genre] += rating
        else:
            genre_ratings[genre] = rating

# Create a DataFrame for genre rankings
genre_rankings = pd.DataFrame(list(genre_ratings.items()), columns=['Genre', 'Total Weighted Score'])

# Sort the DataFrame by total weighted score in descending order
genre_rankings = genre_rankings.sort_values(by='Total Weighted Score', ascending=False)

# Print or visualize the genre rankings
print(genre_rankings)

# Optional: Plot a bar chart of genre rankings
plt.figure(figsize=(10, 6))
plt.bar(genre_rankings['Genre'], genre_rankings['Total Weighted Score'], color='skyblue')
plt.title('Genre Rankings based on Movie Popularity Ratings')
plt.xlabel('Genre')
plt.ylabel('Total Weighted Score')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
