import re

class GrammarChecker:
    def __init__(self, rules):
        self.rules = rules

    def check_grammar(self, sentence):
        for pattern, correction in self.rules.items():
            sentence = re.sub(pattern, correction, sentence)
        return sentence

    @staticmethod
    def load_rules_from_file(file_path):
        rules = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                label, sentence = line.strip().split(maxsplit=1)
                if label == "0":  # Incorrect sentences
                    correct_version = sentence.replace(" ", "")  # Example transformation
                    pattern = re.escape(sentence)
                    rules[pattern] = correct_version
        return rules