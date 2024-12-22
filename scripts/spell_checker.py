# spell_checker.py
import difflib

class SpellChecker:
    def __init__(self, dictionary_path):
        with open(dictionary_path, 'r', encoding='utf-8') as f:
            self.dictionary = set(f.read().splitlines())

    def check_spelling(self, text):
        words = text.split()
        corrected_words = [self.correct_word(word) for word in words]
        return ' '.join(corrected_words)

    def correct_word(self, word):
        if word in self.dictionary:
            return word
        suggestions = difflib.get_close_matches(word, self.dictionary, n=1)
        return suggestions[0] if suggestions else word