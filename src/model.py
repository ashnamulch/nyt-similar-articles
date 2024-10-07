from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# Load Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load embeddings from a file or calculate and save them
# Encode article contents using BERT
def load_embeddings(df, embeddings_file):
    if os.path.exists(embeddings_file):
        print('Loading embeddings from file...')
        embeddings = np.load(embeddings_file, allow_pickle=True)
        if len(embeddings) == len(df):
            df['embeddings'] = list(embeddings)
        else:
            print('Calculating embeddings...')
            df['embeddings'] = df['content'].apply(lambda x: model.encode(x))
            np.save(embeddings_file, df['embeddings'].tolist())
    else:
        print('Calculating embeddings...')
        df['embeddings'] = df['content'].apply(lambda x: model.encode(x))

        # Save embeddings to a .npy file
        np.save(embeddings_file, df['embeddings'].tolist())
    return df['embeddings']

# Function to find similar articles based on a query using BERT
def find_similar_articles_bert(query, df, top_n=5):
    # Encode the user query
    query_embedding = model.encode(query)

    # Calculate cosine similarity between query and article embeddings
    embeddings_matrix = df['embeddings'].tolist() # Convert embeddings to a list
    cosine_similarities = cosine_similarity([query_embedding], embeddings_matrix).flatten()

    # Get the top-n most similar articles
    similar_indices = cosine_similarities.argsort()[::-1]

    top_articles = []
    printed_titles = set()
    count = 0
    for idx in similar_indices:
        if count >= top_n:
            break
        title = df.iloc[idx]['title']
        if title not in printed_titles:
            printed_titles.add(title)
            top_articles.append({
                'title': df.iloc[idx]['title'],
                'url': df.iloc[idx]['url'],
                'similarity': cosine_similarities[idx]
            })
            count += 1

    return top_articles

