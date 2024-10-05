import pandas as pd
import json
import os
from scraper import scrape_nyt_section_articles
from model import load_embeddings, find_similar_articles
from newspaper import Article

# Function to extract content and title from an article URL
def extract_article_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text, article.title
    except:
        return None, None
    
# Scrape and save articles
def load_or_scrape_articles(sections, articles_file='nyt_articles.json', max_pages=10):
    if os.path.exists('articles_file'):
        print('Loading articles from file...')
        with open(articles_file, 'r') as f:
            articles_data = json.load(f)
    else:
        print('Scraping articles...')
        all_articles = []
        for section_url in sections:
            section_articles = scrape_nyt_section_articles(section_url, max_pages=10)
            all_articles.extend(section_articles)

        # Extract content from all articles
        articles_data = []
        for url in all_articles:
            text, title = extract_article_content(url)
            if text and title: # Only save if both text and title are available
                articles_data.append({'url': url, 'title': title, 'content': text})

        # Save scraped articles to a json file
        with open(articles_file, 'w') as f:
            json.dump(articles_data, f)

    # Save the articles to a DataFrame
    df = pd.DataFrame(articles_data)
    return df

# Main script
if __name__ == '__main__':
    # List of NYT sections to scrape
    sections = [
        'https://www.nytimes.com/section/world',
        'https://www.nytimes.com/section/business',
        'https://www.nytimes.com/section/politics',
        'https://www.nytimes.com/section/us',
        'https://www.nytimes.com/section/sports',
        'https://www.nytimes.com/section/health',
        'https://www.nytimes.com/section/nyregion',
        'https://www.nytimes.com/section/opinion',
        'https://www.nytimes.com/section/technology',
        'https://www.nytimes.com/section/science',
        'https://www.nytimes.com/section/arts',
        'https://www.nytimes.com/section/books',
        'https://www.nytimes.com/section/style',
        'https://www.nytimes.com/section/food',
        'https://www.nytimes.com/section/travel',
        'https://www.nytimes.com/section/magazine',
        'https://www.nytimes.com/section/t-magazine',
        'https://www.nytimes.com/section/realestate'
    ]  

    df = load_or_scrape_articles(sections)
    print(f'Number of articles: {df.shape[0]}')

    # Load embeddings
    embeddings_file = 'nyt_embeddings.npy'
    load_embeddings(df, embeddings_file)

    # Query example
    user_query = 'mental health during adolescence'
    similar_articles = find_similar_articles(user_query, df)

    for article in similar_articles:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        print(f"Similarity: {article['similarity']:.4f}\n")