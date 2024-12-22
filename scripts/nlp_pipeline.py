import os
from spellchecker import SpellChecker
import stanza

# Initialize Stanza for Sinhala NLP
stanza.download('si')  # Ensure the Sinhala model is downloaded
nlp = stanza.Pipeline('si', processors='tokenize,pos')

# Load custom dictionary for spelling correction
spell = SpellChecker(language=None)
dictionary_path = "../dictionaries/sinhala_dictionary.txt"
with open(dictionary_path, "r", encoding="utf-8") as f:
    sinhala_words = f.read().splitlines()
    spell.word_frequency.load_words(sinhala_words)

# Function to correct spelling errors
def correct_spelling(word):
    return spell.correction(word) if word not in sinhala_words else word

# Function to detect and correct subject-verb agreement errors
def correct_subject_verb_agreement(parsed_tokens):
    corrections = {
        "අපි පාසල් යයි": "අපි පාසල් යමු",
        "මම පාඩම් කරමු": "මම පාඩම් කරමි",
    }

    # Combine tokens into a sentence for rule checking
    sentence = " ".join([token.text for token in parsed_tokens])
    for incorrect, correct in corrections.items():
        if incorrect in sentence:
            sentence = sentence.replace(incorrect, correct)

    return sentence

# Function to detect and correct tense errors
def correct_tense_errors(parsed_tokens):
    corrections = {
        "ඔහු ඊයේ පාසල් යයි": "ඔහු ඊයේ පාසල් ගියේය.",
    }

    # Combine tokens into a sentence for rule checking
    sentence = " ".join([token.text for token in parsed_tokens])
    for incorrect, correct in corrections.items():
        if incorrect in sentence:
            sentence = sentence.replace(incorrect, correct)

    return sentence

# NLP pipeline for spelling and grammar correction
def nlp_pipeline(sentence):
    # Tokenize and process with Stanza
    doc = nlp(sentence)

    # Correct spelling for each token
    corrected_tokens = []
    for sentence in doc.sentences:
        for token in sentence.tokens:
            corrected_word = correct_spelling(token.text)
            corrected_tokens.append(corrected_word)

    # Recombine corrected tokens into a single sentence
    corrected_sentence = " ".join(corrected_tokens)

    # Parse corrected sentence with Stanza
    doc = nlp(corrected_sentence)

    # Correct grammar errors
    for sentence in doc.sentences:
        corrected_sentence = correct_subject_verb_agreement(sentence.tokens)
        corrected_sentence = correct_tense_errors(sentence.tokens)

    return corrected_sentence

if __name__ == "__main__":
    # Test the pipeline
    test_sentence = "අපි පාසල් යයි"
    corrected_sentence = nlp_pipeline(test_sentence)
    print("Original:", test_sentence)
    print("Corrected:", corrected_sentence)
