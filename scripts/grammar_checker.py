from sinling import SinhalaTokenizer
from language_tool_python import LanguageTool

def initialize_tools():
    tokenizer = SinhalaTokenizer()
    grammar_tool = LanguageTool('si')  # Sinhala language model.
    return tokenizer, grammar_tool

def grammar_check(text, grammar_tool):
    matches = grammar_tool.check(text)
    corrections = []
    for match in matches:
        if match.replacements:
            corrections.append({
                'error': match.context,
                'suggestion': match.replacements[0]
            })
    return corrections

if __name__ == "__main__":
    tokenizer, grammar_tool = initialize_tools()
    text = "අපි පාසල් යයි"
    corrections = grammar_check(text, grammar_tool)
    print(f"Grammar Corrections: {corrections}")
