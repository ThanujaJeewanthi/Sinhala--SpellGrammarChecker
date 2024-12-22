from spell_checker import initialize_symspell, spell_check
from grammar_checker import initialize_tools, grammar_check

def nlp_pipeline(text):
    sym_spell = initialize_symspell()
    tokenizer, grammar_tool = initialize_tools()

    # Step 1: Spell Check
    spell_corrected_text = spell_check(text, sym_spell)

    # Step 2: Grammar Check
    grammar_corrections = grammar_check(spell_corrected_text, grammar_tool)

    return spell_corrected_text, grammar_corrections

if __name__ == "__main__":
    text = "අපි පාසල් යයි"
    spell_corrected_text, grammar_corrections = nlp_pipeline(text)
    print(f"Spell Corrected: {spell_corrected_text}")
    print(f"Grammar Corrections: {grammar_corrections}")
