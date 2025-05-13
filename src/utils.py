def load_word_list():
    with open('words.txt', 'r') as f:
        return [line.strip() for line in f]
