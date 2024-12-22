import tkinter as tk
from tkinter import scrolledtext
from spell_and_grammar_checker import SpellAndGrammarChecker

class SinhalaSpellGrammarCheckerApp:
    def __init__(self, root, dictionary_path, rules_path):
        self.root = root
        self.root.title("Sinhala Spell and Grammar Checker")

        # Initialize the combined checker
        self.checker = SpellAndGrammarChecker(dictionary_path, rules_path)

        # Input text label
        self.input_label = tk.Label(root, text="Enter text:")
        self.input_label.pack()

        # Input text box
        self.input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
        self.input_text.pack()

        # Check button
        self.check_button = tk.Button(root, text="Check", command=self.check_text)
        self.check_button.pack()

        # Output text label
        self.output_label = tk.Label(root, text="Corrected text:")
        self.output_label.pack()

        # Output text box (read-only)
        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10, state='disabled')
        self.output_text.pack()

    def check_text(self):
        # Get the input text
        input_text = self.input_text.get("1.0", tk.END).strip()
        
        # Process the text using spell and grammar checker
        corrected_text = self.checker.check_text(input_text)
        
        # Display corrected text
        self.output_text.configure(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, corrected_text)
        self.output_text.configure(state='disabled')

if __name__ == "__main__":
    # Paths to dictionary and grammar rules
    dictionary_path = "E:/Semester 7/EC9640_AI/Spelling_and_Grammar_Checker_Sinhala/dictionaries/sinhala_dictionary.txt"
    rules_path = "sentences.txt"
    
    # Initialize the Tkinter app
    root = tk.Tk()
    app = SinhalaSpellGrammarCheckerApp(root, dictionary_path, rules_path)
    root.mainloop()
