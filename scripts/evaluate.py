from nlp_pipeline import nlp_pipeline

def evaluate_accuracy(paragraphs):
    total_errors = 0
    corrected_errors = 0

    for text in paragraphs:
        spell_corrected_text, grammar_corrections = nlp_pipeline(text)
        print(f"Original: {text}")
        print(f"Corrected: {spell_corrected_text}")
        print(f"Corrections: {grammar_corrections}")
        total_errors += len(grammar_corrections)
        corrected_errors += sum(1 for correction in grammar_corrections if correction)

    accuracy = (corrected_errors / total_errors) * 100 if total_errors > 0 else 100
    print(f"Accuracy: {accuracy:.2f}%")
    return accuracy

if __name__ == "__main__":
    paragraphs = [
        "මම පාඩම් කරමු",
        "ඔහු ඊයේ පාසල් යයි",
        "අපි පාසල් යයි"
    ]
    evaluate_accuracy(paragraphs)
