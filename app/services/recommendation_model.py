from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class RecommendationModel:
    def __init__(self):
        self.books_df = None
        self.tfidf_matrix = None

    def train(self, books_data):
        self.books_df = pd.DataFrame(books_data)
        tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf.fit_transform(self.books_df['genre'])

    def get_recommendations(self, book_id, top_n=5):
        book_index = self.books_df[self.books_df['id'] == book_id].index[0]
        cosine_similarities = cosine_similarity(self.tfidf_matrix[book_index], self.tfidf_matrix).flatten()
        related_book_indices = cosine_similarities.argsort()[:-top_n-1:-1]
        return self.books_df.iloc[related_book_indices]['id'].tolist()

recommendation_model = RecommendationModel()
