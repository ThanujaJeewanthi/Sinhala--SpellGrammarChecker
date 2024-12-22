from spellchecker import SpellChecker
import os

# Load the custom dictionary
spell = SpellChecker(language=None)
dictionary_path = "../dictionaries/sinhala_dictionary.txt"
with open(dictionary_path, "r", encoding="utf-8") as f:
    sinhala_words = f.read().splitlines()
    spell.word_frequency.load_words(sinhala_words)

# Correct spelling in a sentence
def correct_spelling(sentence):
    words = sentence.split()
    corrected_words = [
        spell.correction(word) if word not in sinhala_words else word for word in words
    ]
    return " ".join(corrected_words)

if __name__ == "__main__":
    test_sentence = "වාහන පොත බලා ගෙදර වේගයෙන් යනලදී"
    print("Original:", test_sentence)
    print("Corrected:", correct_spelling(test_sentence))
