import requests
from bs4 import BeautifulSoup

def get_meaning_fallback(word):
    try:
        url = f'https://www.dictionary.com/browse/{word}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return f"Scraping Error: HTTP {response.status_code}"

        soup = BeautifulSoup(response.text, 'html.parser')
        meaning_tag = soup.find('span', class_='one-click-content')

        if meaning_tag:
            return f"Meaning (via Scraping): {meaning_tag.text.strip()}"
        else:
            return "Scraping Fallback: No meaning found."

    except requests.exceptions.RequestException as e:
        return f"Scraping Error: {e}"
