import tkinter as tk
from tkinter import scrolledtext, messagebox
from nlp_pipeline import nlp_pipeline


def process_text():
    input_text = input_text_area.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text!")
        return

    # Run the NLP pipeline
    spell_corrected_text, grammar_corrections = nlp_pipeline(input_text)

    # Display results
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.END, f"Spell Corrected Text:\n{spell_corrected_text}\n\n")
    output_text_area.insert(tk.END, "Grammar Corrections:\n")
    for correction in grammar_corrections:
        output_text_area.insert(tk.END, f"Error: {correction['error']}\n")
        output_text_area.insert(tk.END, f"Suggestion: {correction['suggestion']}\n\n")


# Create the main Tkinter window
root = tk.Tk()
root.title("Sinhala Spell and Grammar Checker")

# Input Text Area
input_label = tk.Label(root, text="Enter Text:")
input_label.pack()
input_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
input_text_area.pack(pady=10)

# Process Button
process_button = tk.Button(root, text="Check Text", command=process_text)
process_button.pack(pady=5)

# Output Text Area
output_label = tk.Label(root, text="Output:")
output_label.pack()
output_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15, state="normal")
output_text_area.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
