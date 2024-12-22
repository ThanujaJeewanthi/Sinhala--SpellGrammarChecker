from scripts.spell_and_grammar_checker import SpellAndGrammarChecker

def evaluate_accuracy(paragraphs, ground_truths, dictionary_path):
    checker = SpellAndGrammarChecker(dictionary_path)

    correct = 0
    for i, paragraph in enumerate(paragraphs):
        corrected_text = checker.check_text(paragraph)
        print(f"Original: {paragraph}")
        print(f"Corrected: {corrected_text}")
        print(f"Expected: {ground_truths[i]}\n")
        
        if corrected_text.strip() == ground_truths[i].strip():
            correct += 1

    accuracy = (correct / len(paragraphs)) * 100
    return accuracy

if __name__ == "__main__":
    paragraphs = [
        "මම පන්සල් යන්නෙ",
        "අපි ගමනක් යමුද",
    ]
    ground_truths = [
        "මම පන්සලට යන්නෙ.",
        "අපි ගමනක් යමුද?",
    ]

    accuracy = evaluate_accuracy(paragraphs, ground_truths, "dictionaries/sinhala_dictionary.txt")
    print(f"Accuracy: {accuracy}%")
