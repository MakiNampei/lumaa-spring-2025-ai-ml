import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import argparse

df = pd.read_csv('data/movies.csv')
df = df[['title', 'description']].dropna()

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

def recommend_movies(query, top_n=5):
    query_vec = vectorizer.transform([query])  
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]  
    return df.iloc[top_indices][['title', 'description']]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="describe")
    args = parser.parse_args()
    
    recommendations = recommend_movies(args.query)
    print(recommendations)

