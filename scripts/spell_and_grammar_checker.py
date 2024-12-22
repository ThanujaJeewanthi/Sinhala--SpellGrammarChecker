# spell_and_grammar_checker.py
from spell_checker import SpellChecker
from grammar_checker import GrammarChecker

class SpellAndGrammarChecker:
    def __init__(self, dictionary_path, rules_path):
        self.spell_checker = SpellChecker(dictionary_path)
        self.grammar_checker = GrammarChecker(GrammarChecker.load_rules_from_file(rules_path))

    def check_text(self, text):
        spell_checked_text = self.spell_checker.check_spelling(text)
        sentences = spell_checked_text.split('.')
        corrected_sentences = [self.grammar_checker.check_grammar(sentence.strip()) for sentence in sentences if sentence.strip()]
        return '. '.join(corrected_sentences) + '.'