import re  # Import for regular expressions
import difflib  # Import for finding close matches

class SpellAndGrammarChecker:
    def __init__(self, dictionary_path, rules_path):
        self.dictionary = self.load_dictionary(dictionary_path)  # Load dictionary for spell checking
        self.grammar_rules = self.load_grammar_rules(rules_path)  # Load grammar correction rules

    def check_text(self, text):
        # Perform spell checking
        spell_checked_text = self.check_spelling(text)

        # Split sentences for grammar checking
        sentences = re.split(r'(?<=[.!?]) +', spell_checked_text)

        # Apply grammar rules to each sentence
        corrected_sentences = [self.apply_grammar_rules(sentence) for sentence in sentences]

        # Combine sentences back into text
        return ' '.join(corrected_sentences)

    def check_spelling(self, text):
        """Spell-check each word in the text using the dictionary."""
        words = text.split()
        corrected_words = [
            self.correct_word(word) for word in words
        ]  # Correct each word
        return ' '.join(corrected_words)

    def correct_word(self, word):
        """Correct a single word if it is misspelled."""
        if word in self.dictionary:  # If the word is correct, return it
            return word
        # If misspelled, find the closest match
        suggestions = difflib.get_close_matches(word, self.dictionary, n=1)
        return suggestions[0] if suggestions else word  # Use suggestion if available

    def apply_grammar_rules(self, sentence):
        """Apply grammar correction rules to a sentence."""
        for incorrect, correct in self.grammar_rules.items():
            sentence = re.sub(rf'\b{re.escape(incorrect)}\b', correct, sentence)
        return sentence

    def load_dictionary(self, file_path):
        """Load words from the dictionary file into a set."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f)

    def load_grammar_rules(self, file_path):
        """Load grammar rules from the file."""
        rules = {}
        temp_map = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                label, text = line.strip().split(maxsplit=1)
                if label == "0":
                    temp_map[text] = None
                elif label == "1":
                    for incorrect in list(temp_map):
                        if temp_map[incorrect] is None:
                            temp_map[incorrect] = text
                            break
        for incorrect, correct in temp_map.items():
            if correct:
                rules[incorrect] = correct
        return rules
