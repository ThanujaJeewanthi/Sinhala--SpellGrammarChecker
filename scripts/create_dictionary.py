import os
import re

# Paths to data folder and dictionary file
data_folder = os.path.join(os.getcwd(), "..", "data")  # Adjusted for folder structure
dictionary_file = os.path.join(os.getcwd(), "..", "dictionaries", "sinhala_dictionary.txt")


def clean_and_tokenize(text):
    # Remove punctuation and extra whitespace
    text = re.sub(r"[^\u0D80-\u0DFF\s]", "", text)  # Keep only Sinhala characters
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    # Tokenize the text
    words = text.split()
    return words

def update_dictionary():
    words_set = set()

    # Load existing dictionary words (if the file exists)
    if os.path.exists(dictionary_file):
        with open(dictionary_file, "r", encoding="utf-8") as f:
            existing_words = f.read().splitlines()
            words_set.update(existing_words)

    # Check if the data folder exists
    if not os.path.exists(data_folder):
        print(f"Error: The folder '{data_folder}' does not exist.")
        return

    # Read all text files in the data folder
    for file in os.listdir(data_folder):
        if file.endswith(".txt"):
            file_path = os.path.join(data_folder, file)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                # Tokenize and add words to the set
                words = clean_and_tokenize(text)
                words_set.update(words)

    # Save the updated dictionary to the dictionary file
    os.makedirs(os.path.dirname(dictionary_file), exist_ok=True)  # Create the dictionaries folder if it doesn't exist
    with open(dictionary_file, "w", encoding="utf-8") as f:
        for word in sorted(words_set):  # Sort for consistency
            f.write(word + "\n")
    
    print(f"Dictionary updated with {len(words_set)} unique words and saved to {dictionary_file}")

if __name__ == "__main__":
    update_dictionary()
