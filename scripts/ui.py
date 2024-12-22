import tkinter as tk
from tkinter import scrolledtext
from nlp_pipeline import run_spell_and_grammar_check, auto_correct_text, auto_correct_grammar_text

def run_spell_and_grammar_check_gui():
    input_text = text_area.get("1.0", tk.END)
    dictionary_path = 'path/to/sinhala_dictionary.txt'
    
    misspelled_words, grammar_issues = run_spell_and_grammar_check(input_text, dictionary_path)
    
    result_area.delete("1.0", tk.END)
    
    if not misspelled_words:
        result_area.insert(tk.END, "No spelling errors found!\n")
    else:
        result_area.insert(tk.END, "Misspelled words:\n")
        result_area.insert(tk.END, ", ".join(misspelled_words) + "\n")
    
    if not grammar_issues:
        result_area.insert(tk.END, "No grammar issues found!\n")
    else:
        result_area.insert(tk.END, "Grammar issues:\n")
        result_area.insert(tk.END, "\n".join(grammar_issues) + "\n")

def auto_correct_text_gui():
    input_text = text_area.get("1.0", tk.END)
    dictionary_path = 'path/to/sinhala_dictionary.txt'
    corrected_text = auto_correct_text(input_text, dictionary_path)
    
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, corrected_text)

def auto_correct_grammar_text_gui():
    input_text = text_area.get("1.0", tk.END)
    corrected_text = auto_correct_grammar_text(input_text)
    
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, corrected_text)

def reset_text():
    text_area.delete("1.0", tk.END)
    result_area.delete("1.0", tk.END)

# GUI setup
root = tk.Tk()
root.title("Sinhala Spell and Grammar Checker")
root.geometry("500x500")

# Frame for input and buttons
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Input area for the user to type text
text_area_label = tk.Label(frame, text="Enter Sinhala text:")
text_area_label.pack()

text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=10)
text_area.pack(pady=5)

# Buttons for checking and correcting text
check_button = tk.Button(frame, text="Check Spelling & Grammar", command=run_spell_and_grammar_check_gui)
check_button.pack(pady=5)

auto_correct_button = tk.Button(frame, text="Auto Correct Spelling", command=auto_correct_text_gui)
auto_correct_button.pack(pady=5)

auto_correct_grammar_button = tk.Button(frame, text="Auto Correct Grammar", command=auto_correct_grammar_text_gui)
auto_correct_grammar_button.pack(pady=5)

reset_button = tk.Button(frame, text="Reset", command=reset_text)
reset_button.pack(pady=5)

# Frame for displaying results
result_label = tk.Label(root, text="Results:")
result_label.pack(pady=5)

result_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
result_area.pack(pady=5)

root.mainloop()
