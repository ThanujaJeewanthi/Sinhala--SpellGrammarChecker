### model_training.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Load data
data_path = "sentences.txt"
data = []

with open(data_path, "r", encoding="utf-8") as file:
    for line in file:
        label, sentence = line.split(maxsplit=1)
        data.append((int(label), sentence.strip()))

data = pd.DataFrame(data, columns=["label", "sentence"])

# Vectorize sentences
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["sentence"])
y = data["label"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model and vectorizer
with open("../grammar_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("../vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Model and vectorizer saved successfully!")