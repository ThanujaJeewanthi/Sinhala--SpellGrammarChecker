# Rule-based grammar correction

# Correct subject-verb agreement
def correct_subject_verb_agreement(sentence):
    corrections = {
        "අපි පාසල් යයි": "අපි පාසල් යමු",
        "මම පාඩම් කරමු": "මම පාඩම් කරමි",
    }
    for incorrect, correct in corrections.items():
        if incorrect in sentence:
            sentence = sentence.replace(incorrect, correct)
    return sentence

# Correct tense errors
def correct_tense_errors(sentence):
    corrections = {
        "ඔහු ඊයේ පාසල් යයි": "ඔහු ඊයේ පාසල් ගියේය.",
    }
    for incorrect, correct in corrections.items():
        if incorrect in sentence:
            sentence = sentence.replace(incorrect, correct)
    return sentence

# Combine grammar corrections
def correct_grammar(sentence):
    sentence = correct_subject_verb_agreement(sentence)
    sentence = correct_tense_errors(sentence)
    return sentence

if __name__ == "__main__":
    test_sentence = "ඔහු ඊයේ පාසල් යයි"
    print("Original:", test_sentence)
    print("Grammar Corrected:", correct_grammar(test_sentence))
