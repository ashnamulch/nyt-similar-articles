import requests
from bs4 import BeautifulSoup
import time

# Function to scrape article URLs from a section page
def scrape_nyt_section_articles(section_url, max_pages=10):
    response = requests.get(section_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all article links
    article_links = []
    page_number = 1

    while page_number <= max_pages:
        url = f'{section_url}?page={page_number}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all article links on the current page
        for article in soup.find_all('a', href=True):
            link = article['href']
            if link.startswith('/'):
                link = f'https://nytimes.com{link}'
            if '/202' in link: # Fetch valid article URLs (with year in the URL)
                article_links.append(link)
    
        print(f'Scraped page {page_number} of {section_url}. Found {len(article_links)} so far.')
        page_number += 1

        # To prevent overloading the server, provide a short delay
        time.sleep(1)
    
    return article_links


