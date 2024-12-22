from scripts.spell_checker import SpellChecker
from scripts.grammar_checker import SinhalaGrammarCorrector

class NLPPipeline:
    def __init__(self, dictionary_path, model_folder):
        self.spell_checker = SpellChecker(dictionary_path)
        self.grammar_checker = SinhalaGrammarCorrector(model_folder)

    def process_text(self, text):
        corrected_spelling = self.spell_checker.correct_spelling(text)
        corrected_grammar = self.grammar_checker.correct_sentence(corrected_spelling)
        return corrected_grammar
