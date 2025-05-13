📚 Word Lookup Dictionary
A desktop application for online lookup of English words, providing:
- Meaning
- Examples
- Synonyms
- Etymology
- Spelling correction
- Auto-suggestions
- Pronunciation
- Dark/Light theme toggle

🚀 Features

- 🔍 Word Lookup: Uses Oxford Dictionaries API and web scraping as fallback.
- 🧠 Spelling Correction: Uses Edit Distance algorithm.
- 💡 Auto Suggestion: Fast lookup using Trie data structure.
- 🗣️ Pronunciation: Listen to correct word pronunciation.
- 🌗 Dark/Light Theme: Toggle between dark and light mode.

🛠 Technologies Used

- Python 3.8+
- PyQt5 (GUI)
- Oxford Dictionaries API
- BeautifulSoup (Web scraping)
- SpaCy (Fallback data extraction)
- Trie (Data structure for suggestions)
- Edit Distance Algorithm (Spelling correction)
- gTTS (Pronunciation)
- playsound (Audio playback)

📂 Project Structure

| Folder / File         | Description                 |
| ----------------------|---------------------------- |
| src/                  | Source code directory       |
| ├── dictionary_app.py | Main GUI Application        |
| ├── oxford_api.py     | Oxford API Integration      |
| ├── scraper.py        | Web Scraping Fallback       |
| ├── trie.py           | Trie Data Structure         |
| ├── edit_distance.py  | Edit Distance Algorithm     |
| ├── utils.py          | Theme and Utility Functions |
| ├── words.txt         | Word List for Trie          |
| └── .env              | API Keys (Optional)         |
| requirements.txt      | Python dependencies         |
| README.md             | Project Documentation       |

🔑 Oxford API Setup

1. Create a free account at: https://developer.oxforddictionaries.com/

2. Get your `APP_ID` and `APP_KEY`.

3. Open `src/oxford_api.py` and add your credentials:

python

APP_ID = 'cc3c7d27'

APP_KEY = 'efbbc5edc75eebb22ede3aa057874553'

💻 How to Run Locally (Step by Step)
1. Clone the Repository
bash:-

git clone https://github.com/your-username/word-lookup-dictionary.git

cd word-lookup-dictionary

2. Setup Virtual Environment
bash:-
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate


3. Install Dependencies
bash:-

pip install -r requirements.txt

python -m spacy download en_core_web_sm

4. Run the Application
bash:-

cd src

python dictionary_app.py

🔧 Optional Configurations
🔁 Switch between Sandbox and Production API

In src/oxford_api.py:
python
USE_SANDBOX = True  # For safe testing

False to use production/live data

🌐 Web Scraping Fallback
If Oxford API data is missing, the app will attempt to scrape definitions from the web.

💼 Build Executable (Windows)(Optional)

Install PyInstaller

bash:-

pip install pyinstaller

Build Executable

bash:-

cd src

pyinstaller --onefile --noconsole dictionary_app.py


#Executable will appear in dist/ folder.








