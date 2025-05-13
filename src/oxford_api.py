import requests

APP_ID = 'cc3c7d27'
APP_KEY = 'efbbc5edc75eebb22ede3aa057874553'
USE_SANDBOX = False  # Set False if you have live keys

OXFORD_BASE_URL = 'https://od-api-sandbox.oxforddictionaries.com/api/v2/entries/en-gb' if USE_SANDBOX else 'https://od-api.oxforddictionaries.com/api/v2/entries/en-gb'
FREE_DICT_URL = 'https://api.dictionaryapi.dev/api/v2/entries/en'

def get_oxford_data(word):
    url = f'{OXFORD_BASE_URL}/{word.lower()}'
    headers = {
        'cc3c7d27': APP_ID,
        'efbbc5edc75eebb22ede3aa057874553': APP_KEY
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return parse_oxford_response(response.json())
        elif response.status_code == 403:
            return f"Oxford API Error: 403 Forbidden - Check API Keys or Endpoint"
        elif response.status_code == 404:
            return f"Oxford API Error: 404 - Word not found"
        else:
            return f"Oxford API Error: HTTP {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Oxford API Error: {e}"

def parse_oxford_response(data):
    try:
        entries = data['results'][0]['lexicalEntries'][0]['entries'][0]
        senses = entries['senses'][0]
        meaning = senses['definitions'][0] if 'definitions' in senses else "No definition found."

        examples = []
        if 'examples' in senses:
            examples = [ex['text'] for ex in senses['examples']]

        synonyms = []
        if 'synonyms' in senses:
            synonyms = [syn['text'] for syn in senses['synonyms']]

        etymology = entries.get('etymologies', ['No etymology found.'])[0]

        return f"Meaning: {meaning}\nExamples: {examples}\nSynonyms: {synonyms}\nEtymology: {etymology}"
    except Exception:
        return "Error parsing Oxford API response."

def get_free_dictionary_data(word):
    try:
        response = requests.get(f'{FREE_DICT_URL}/{word.lower()}')
        if response.status_code == 200:
            data = response.json()[0]
            meaning = data['meanings'][0]['definitions'][0]['definition']
            example = data['meanings'][0]['definitions'][0].get('example', 'No example found.')
            synonyms = data['meanings'][0]['definitions'][0].get('synonyms', [])
            return f"Meaning: {meaning}\nExample: {example}\nSynonyms: {synonyms}"
        elif response.status_code == 404:
            return "Free Dictionary: Word not found."
        else:
            return f"Free Dictionary: HTTP {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Free Dictionary Error: {e}"

def lookup_word(word):
    print("[INFO] Trying Oxford API...")
    oxford_result = get_oxford_data(word)
    if "Oxford API Error" in oxford_result:
        print(oxford_result)
        print("[INFO] Switching to Free Dictionary API...")
        free_result = get_free_dictionary_data(word)
        if "Free Dictionary" in free_result:
            print(free_result)
            print("[INFO] Attempting scraping fallback...")
            from scraper import get_meaning_fallback
            scrape_result = get_meaning_fallback(word)
            return scrape_result or "No meaning found via scraping."
        else:
            return free_result
    else:
        return oxford_result
