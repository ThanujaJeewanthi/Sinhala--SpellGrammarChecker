from symspellpy import SymSpell, Verbosity

def initialize_symspell():
    sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
    dictionary_path = "../dictionaries/sinhala_dictionary.txt"
    sym_spell.load_dictionary(dictionary_path, 0, 1)
    return sym_spell

def spell_check(text, sym_spell):
    corrected_words = []
    for word in text.split():
        suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        if suggestions:
            corrected_words.append(suggestions[0].term)
        else:
            corrected_words.append(word)
    return " ".join(corrected_words)

if __name__ == "__main__":
    sym_spell = initialize_symspell()
    text = "මම පාඩම් කරමු"
    corrected_text = spell_check(text, sym_spell)
    print(f"Corrected Text: {corrected_text}")
