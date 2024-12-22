# spell_checker.py
import re
import difflib

def preprocess_text(text):
    """
    Preprocess the given text by removing unwanted characters and normalizing it.
    This function will keep only Sinhala characters and spaces.
    """
    text = re.sub(r'[^\u0D80-\u0DFF\s]', '', text)
    text = text.strip().lower()
    return text

def tokenize(text):
    """
    Tokenize the text by splitting it into individual words based on spaces.
    """
    return text.split()

def load_dictionary(dictionary_path):
    """
    Load the Sinhala dictionary from a file and return it as a set.
    """
    with open(dictionary_path, 'r', encoding='utf-8') as f:
        return set(f.read().splitlines())

def spell_check(text, dictionary):
    """
    Check for misspelled words in the given text.
    """
    words = tokenize(preprocess_text(text))
    misspelled = [word for word in words if word not in dictionary]
    return misspelled

def auto_correct(text, dictionary):
    """
    Auto correct the misspelled words by replacing them with the closest match from the dictionary.
    """
    words = tokenize(preprocess_text(text))
    corrected_words = []
    for word in words:
        if word in dictionary:
            corrected_words.append(word)
        else:
            closest_matches = difflib.get_close_matches(word, dictionary, n=1)
            if closest_matches:
                corrected_words.append(closest_matches[0])
            else:
                corrected_words.append(word)
    return ' '.join(corrected_words)
