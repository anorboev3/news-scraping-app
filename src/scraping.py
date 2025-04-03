from bs4 import BeautifulSoup
import requests

# Function to scrape an article from a given URL
# Extracts the headline and content of the article
# Returns the headline and content as a tuple
def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headline = soup.find('h1').get_text() if soup.find('h1') else "No headline found"
    paragraphs = soup.find_all('p')
    content = ' '.join([p.get_text() for p in paragraphs])
    return headline, content