from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QPlainTextEdit, QHBoxLayout
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from oxford_api import lookup_word
from tts import speak_word

class DictionaryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word Lookup Dictionary")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        # Input field and buttons
        input_layout = QHBoxLayout()
        self.word_input = QLineEdit()
        self.word_input.setPlaceholderText("Enter word...")
        input_layout.addWidget(self.word_input)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_word)
        input_layout.addWidget(self.search_button)

        self.pronounce_button = QPushButton("Pronounce")
        self.pronounce_button.clicked.connect(self.pronounce_word)
        input_layout.addWidget(self.pronounce_button)

        self.theme_button = QPushButton("Toggle Theme")
        self.theme_button.clicked.connect(self.toggle_theme)
        input_layout.addWidget(self.theme_button)

        self.log_button = QPushButton("View Log (Info)")
        self.log_button.clicked.connect(lambda: self.output_area.appendPlainText("[INFO] Check console or log file for detailed debug logs."))
        input_layout.addWidget(self.log_button)

        self.layout.addLayout(input_layout)

        # Output area
        self.output_area = QPlainTextEdit()
        self.output_area.setReadOnly(True)
        self.layout.addWidget(self.output_area)

        self.setLayout(self.layout)
        self.dark_mode = False

        # Initial theme setup
        self.apply_light_theme()

    def search_word(self):
        word = self.word_input.text().strip()
        if not word:
            self.output_area.setPlainText("Please enter a word.")
            return

        self.output_area.setPlainText("Looking up...")
        QApplication.processEvents()

        try:
            result = lookup_word(word)
            self.output_area.setPlainText(result)
            self.log_output("[SUCCESS] Lookup complete.")
        except Exception as e:
            self.output_area.setPlainText(f"An error occurred: {e}")
            self.log_output(f"[ERROR] {e}")

    def pronounce_word(self):
        word = self.word_input.text().strip()
        if not word:
            self.output_area.setPlainText("Please enter a word to pronounce.")
            return

        try:
            speak_word(word)
            self.log_output("[INFO] Pronunciation played.")
        except Exception as e:
            self.output_area.setPlainText(f"Error in pronunciation: {e}")
            self.log_output(f"[ERROR] Pronunciation: {e}")

    def toggle_theme(self):
        if self.dark_mode:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()
        self.dark_mode = not self.dark_mode

    def apply_light_theme(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        palette.setColor(QPalette.Base, QColor(255, 255, 255))
        palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
        palette.setColor(QPalette.Text, QColor(0, 0, 0))
        palette.setColor(QPalette.Button, QColor(240, 240, 240))
        palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        self.setPalette(palette)

        # Update button and input field colors for light theme
        self.word_input.setStyleSheet("background-color: white; color: black; border: 1px solid gray;")
        self.search_button.setStyleSheet("background-color: lightgray; color: black;")
        self.pronounce_button.setStyleSheet("background-color: lightgray; color: black;")
        self.theme_button.setStyleSheet("background-color: lightgray; color: black;")
        self.log_button.setStyleSheet("background-color: lightgray; color: black;")

    def apply_dark_theme(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.Highlight, QColor(142, 45, 197).lighter())
        palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        self.setPalette(palette)

        # Update button and input field colors for dark theme
        self.word_input.setStyleSheet("background-color: #353535; color: white; border: 1px solid gray;")
        self.search_button.setStyleSheet("background-color: #4b4b4b; color: white;")
        self.pronounce_button.setStyleSheet("background-color: #4b4b4b; color: white;")
        self.theme_button.setStyleSheet("background-color: #4b4b4b; color: white;")
        self.log_button.setStyleSheet("background-color: #4b4b4b; color: white;")

    def log_output(self, text):
        self.output_area.appendPlainText(text)
        self.output_area.appendPlainText("-" * 40)

if __name__ == "__main__":
    app = QApplication([])
    window = DictionaryApp()
    window.show()
    app.exec_()
