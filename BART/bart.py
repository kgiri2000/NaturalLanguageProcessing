from transformers import pipeline

# Load pre-trained model from Hugging Face
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define the candidate labels for classification
candidate_labels = ["risk", "safety", "no risk", "procedure"]

# Sample text from the safety manual or any construction document
text = """
Workers should always wear safety helmets when working at heights, as falling debris could cause serious injuries.
"""

# Classify the text
result = classifier(text, candidate_labels)

# Display the result
print(f"Labels: {result['labels']}")
print(f"Scores: {result['scores']}")

# You can interpret the scores to see the most likely category
