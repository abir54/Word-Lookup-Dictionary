from gtts import gTTS
import os

def speak_word(word):
    try:
        tts = gTTS(word)
        tts.save("word.mp3")
        os.system("start word.mp3")  # For Windows, it opens the audio file
    except Exception as e:
        print(f"Error in pronunciation: {e}")
