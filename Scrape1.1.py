import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
base_url = 'https://www.klnews.co.kr'
path = '/news/articleList.html'
full_url = base_url + path

# Parameters for the GET request
params = {
    'view_type': 'sm',
    'sc_word': 'ESG'
}

# Send a HTTP GET request to the URL with parameters
response = requests.get(full_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <h4> elements with class 'titles' which contain the article titles and links
    article_titles = soup.find_all('h4', class_='titles')

    # Check if any articles were found
    if article_titles:
        # Extract links and prepend base URL if necessary
        for title in article_titles:
            a_tag = title.find('a')
            if a_tag:
                link = a_tag['href']
                # Ensure the link is absolute by checking if it already starts with http(s)
                if not link.startswith('http'):
                    link = base_url + link
                print(link)  # Print the full link
    else:
        print("No articles found. Check your selector.")
else:
    print(f"Failed to retrieve page, status code: {response.status_code}")

