# NYT Article Similarity Search

This project scrapes the New York Times website for articles, encodes their content using Sentence-BERT, and allows you to search for similar articles based on a query.

## Features
- Scrapes articles from multiple NYT sections
- Stores and reuses article embeddings for faster searches
- Allows users to search for similar articles using a custom query

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/ashnamulch/nyt-similar-articles.git
   cd nyt-similar-articles/src
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the scraper and search tool:
   ```bash
   python main.py
   ```

## Customizing the User Query
By default, this project allows users to input their own search query for finding similar articles. Follow the steps below to change the query and search for specific articles.
1. Open the main.py file in any text editor or IDE.
   
3. Find the following section in the code:
   ```bash
   # Query example
   user_query = 'renewable energy advancements in 2024'
   ```
   
4. Replace the string with your desired search query. For example:
   ```bash
   user_query = 'new discoveries in space exploration'
   ```
   
5. Save the file and re-run the program:
   ```bash
   python main.py
   ```
   
6. The system will return the top 5 articles most similar to your query

## Example output
After running the script with a query, you will see an output similar to the following. 

**Example query: ``` 'renewable energy advancements in 2024' ```**

```bash
Loading articles from file...
Number of articles: 12644
Loading embeddings from file...
------------------------------------------------------
Title: U.S. Approves Billions in Aid to Restart Michigan Nuclear Plant
URL: https://nytimes.com/2024/09/30/climate/michigan-nuclear-plant-palisades.html
Similarity: 0.4264

Title: Nuclear Power Is the New A.I. Trade. What Could Possibly Go Wrong?
URL: https://nytimes.com/2024/09/27/business/ai-nuclear-power-stocks.html
Similarity: 0.4207

Title: Britain Shuts Down Last Coal Plant, ‘Turning Its Back on Coal Forever’
URL: https://nytimes.com/2024/09/30/climate/britain-last-coal-power-plant.html
Similarity: 0.3964

Title: Biden to Sign Bill Allowing Chip Projects to Skirt Key Environmental Review
URL: https://nytimes.com/2024/10/01/us/politics/biden-semiconductor-environmental-review.html
Similarity: 0.3630

Title: Britain Backs Plan to Store Carbon Dioxide Under the Sea
URL: https://nytimes.com/2024/10/04/business/britain-carbon-capture.html
Similarity: 0.3572
```
