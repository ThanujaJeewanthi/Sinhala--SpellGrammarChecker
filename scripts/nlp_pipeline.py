from spell_checker import spell_check, auto_correct, load_dictionary
from grammar_checker import basic_grammar_check, auto_correct_grammar

def run_spell_and_grammar_check(text, dictionary_path):
    """
    Run the spell and grammar check on the input text and return the results.
    """
    dictionary = load_dictionary(dictionary_path)
    
    # Spell check
    misspelled_words = spell_check(text, dictionary)
    
    # Grammar check
    grammar_issues = basic_grammar_check(text)
    
    return misspelled_words, grammar_issues

def auto_correct_text(text, dictionary_path):
    """
    Automatically correct misspelled words in the input text.
    """
    dictionary = load_dictionary(dictionary_path)
    return auto_correct(text, dictionary)

def auto_correct_grammar_text(text):
    """
    Automatically correct grammar mistakes in the input text.
    """
    return auto_correct_grammar(text)
