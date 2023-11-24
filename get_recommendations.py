import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset (replace this with your own dataset)
data = {
    'User': ['User1', 'User1', 'User2', 'User2', 'User3'],
    'Item': ['Movie1', 'Movie2', 'Movie2', 'Movie3', 'Movie1'],
    'Rating': [5, 4, 3, 2, 5],
    'Genre': ['Action', 'Drama', 'Drama', 'Comedy', 'Action']
}

df = pd.DataFrame(data)

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the item features (in this case, 'Genre')
item_tfidf_matrix = tfidf_vectorizer.fit_transform(df['Genre'])

# Compute the cosine similarity between items based on their TF-IDF features
cosine_similarity = linear_kernel(item_tfidf_matrix, item_tfidf_matrix)

# Function to get recommendations for a given item
def get_recommendations(item_index, cosine_sim=cosine_similarity):
    sim_scores = list(enumerate(cosine_sim[item_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get the top 3 most similar items (excluding itself)
    item_indices = [i[0] for i in sim_scores]
    return df['Item'].iloc[item_indices]

# Example: Get recommendations for 'Movie1'
movie_index = df[df['Item'] == 'Movie1'].index[0]
recommendations = get_recommendations(movie_index)
print(recommendations)
