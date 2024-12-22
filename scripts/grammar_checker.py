import re

class GrammarChecker:
    def __init__(self, rules):
        self.rules = rules

    def check_grammar(self, sentence):
        for incorrect, correct in self.rules.items():
            sentence = re.sub(rf'\b{re.escape(incorrect)}\b', correct, sentence)
        return sentence

    @staticmethod
    def load_rules_from_file(file_path):
        rules = {}
        temp_map = {}  # Temporary map to link incorrect and correct sentences
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                label, text = line.strip().split(maxsplit=1)
                if label == "0":  # Incorrect sentences
                    temp_map[text] = None
                elif label == "1":  # Correct sentences
                    # Assign the correct sentence to the last incorrect sentence
                    for incorrect in list(temp_map):
                        if temp_map[incorrect] is None:
                            temp_map[incorrect] = text
                            break
        # Map incorrect to correct
        for incorrect, correct in temp_map.items():
            if correct:
                rules[incorrect] = correct
        return rules
