
import tkinter as tk
from tkinter import scrolledtext
from spell_and_grammar_checker import SpellAndGrammarChecker

class SinhalaSpellGrammarCheckerApp:
    def __init__(self, root, dictionary_path, rules_path):
        self.root = root
        self.root.title("Sinhala Spell and Grammar Checker")

        self.checker = SpellAndGrammarChecker(dictionary_path, rules_path)

        self.input_label = tk.Label(root, text="Enter text:")
        self.input_label.pack()

        self.input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
        self.input_text.pack()

        self.check_button = tk.Button(root, text="Check", command=self.check_text)
        self.check_button.pack()

        self.output_label = tk.Label(root, text="Corrected text:")
        self.output_label.pack()

        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10, state='disabled')
        self.output_text.pack()

    def check_text(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        corrected_text = self.checker.check_text(input_text)
        self.output_text.configure(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, corrected_text)
        self.output_text.configure(state='disabled')

if __name__ == "__main__":
    dictionary_path = "E:/Semester 7/EC9640_AI/Spelling_and_Grammar_Checker_Sinhala/dictionaries/sinhala_dictionary.txt"
    rules_path = "sentences.txt"
    root = tk.Tk()
    app = SinhalaSpellGrammarCheckerApp(root, dictionary_path, rules_path)
    root.mainloop()