import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape
base_url = 'https://www.klnews.co.kr'
path = '/news/articleList.html'

# Parameters for the GET request
params = {
    'view_type': 'sm',
    'sc_word': '지배구조',
    'page': 1  # Starting page
}

# Set the number of pages you want to scrape
number_of_pages = 27

# Initialize a list to store the scraped data
articles_data = []

# Loop over the range of pages you want to scrape
for page in range(1, number_of_pages + 1):
    # Update the 'page' parameter in the params dictionary
    params['page'] = page

    # Make the GET request
    response = requests.get(f"{base_url}{path}", params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Update this selector based on the actual elements you want to scrape
    articles = soup.select('YOUR_CORRECT_SELECTOR_HERE')

    if articles:
        for article in articles:
            # Extract data from each article
            # Example: title = article.find('h2').get_text()
            # Add the data to your articles_data list
            pass
    else:
        print(f"No articles found on page {page}. Check your selector.")
