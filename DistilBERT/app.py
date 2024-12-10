import streamlit as st
from pdf_utils import extract_text_from_pdf
from transformers import pipeline

# Load the QA model from Hugging Face (DistilBERT fine-tuned for QA)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad", tokenizer="distilbert-base-uncased")

# Streamlit file uploader
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

# Display a prompt for users to ask a question
question = st.text_input("Ask a question about the content:")

if uploaded_file is not None:
    # Extract text from the uploaded PDF
    context = extract_text_from_pdf(uploaded_file)
    st.text_area("Extracted Text", context, height=300)

# If the user asks a question, get the answer
if question and uploaded_file is not None:
    st.write(f"Your question: {question}")

    # Use the QA pipeline to get the answer
    result = qa_pipeline(question=question, context=context)

    # Display the answer
    st.write(f"Answer: {result['answer']}")