from nlp_pipeline import nlp_pipeline

# Load dataset
def load_dataset(file_path):
    dataset = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            label, sentence = line.strip().split(" ", 1)
            dataset.append((int(label), sentence))
    return dataset

# Evaluate the pipeline
def evaluate_pipeline(dataset):
    correct_count = 0
    total_count = len(dataset)

    for label, sentence in dataset:
        corrected_sentence = nlp_pipeline(sentence)
        is_correct = (label == 1)  # Ground truth
        pipeline_correct = (corrected_sentence == sentence)

        if is_correct == pipeline_correct:
            correct_count += 1

    accuracy = (correct_count / total_count) * 100
    print(f"Pipeline Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    # Load the dataset
    dataset = load_dataset("../data/sentences.txt")

    # Evaluate the pipeline
    evaluate_pipeline(dataset)
