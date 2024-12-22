from spell_checker import correct_spelling
from grammar_checker import correct_grammar

def correct_text(text):
    # First, correct spelling
    text = correct_spelling(text)
    # Then, correct grammar
    text = correct_grammar(text)
    return text

if __name__ == "__main__":
    test_text = "උදවු ඔබේ අවශ්යය්."
    corrected_text = correct_text(test_text)
    print(f"Original Text: {test_text}")
    print(f"Final Corrected Text: {corrected_text}")
