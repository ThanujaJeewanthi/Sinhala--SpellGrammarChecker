import re

def preprocess_text(text):
    """
    Preprocess the given text by removing unwanted characters and normalizing it.
    """
    text = text.strip().lower()
    return text

def basic_grammar_check(text):
    """
    Perform a basic grammar check on the given text.
    This function checks for repeated words and punctuation issues.
    """
    grammar_issues = []
    words = text.split()

    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            grammar_issues.append(f"Repeated word: '{words[i]}'")
    
    if not re.match(r'.*[.!?]$', text.strip()):
        grammar_issues.append("The text does not end with proper punctuation (., !, ?).")
    
    return grammar_issues

def auto_correct_grammar(text):
    """
    Automatically correct basic grammar mistakes in the input text.
    This function will correct repeated words and add punctuation if missing.
    """
    words = text.split()
    corrected_words = []

    for i in range(len(words)):
        if i == 0 or words[i] != words[i - 1]:
            corrected_words.append(words[i])

    corrected_text = ' '.join(corrected_words)

    if not re.match(r'.*[.!?]$', corrected_text.strip()):
        corrected_text += '.'

    return corrected_text
