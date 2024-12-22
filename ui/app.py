from flask import Flask, render_template, request
from spell_checker import initialize_spell_checker, spell_check_and_correct
from grammar_checker import initialize_tools, check_grammar_with_tool

app = Flask(__name__)

# Initialize tools
sym_spell = initialize_spell_checker('../dictionaries/sinhala_dictionary.txt')
nlp, tool = initialize_tools()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    text = request.form['text']
    corrected_text = spell_check_and_correct(text, sym_spell)
    grammar_errors = check_grammar_with_tool(corrected_text, tool)
    return render_template('results.html', corrected_text=corrected_text, grammar_errors=grammar_errors)

if __name__ == "__main__":
    app.run(debug=True)
