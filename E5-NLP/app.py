import streamlit as st
import pdfplumber
from transformers import MarianMTModel, MarianTokenizer, pipeline
import re

@st.cache_resource
def load_summarization_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

@st.cache_resource
def load_translation_model():
    model_name = "Helsinki-NLP/opus-mt-en-es"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

def clean_text(text):
    text = re.sub(r"(no,?\s*){2,}", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def summarize_text(text, summarization_pipeline):
    summaries = summarization_pipeline(text, max_length=150, min_length=50, do_sample=False)
    return " ".join([summary["summary_text"] for summary in summaries])

def translate_text(text, model, tokenizer):
    tokenized = tokenizer.prepare_seq2seq_batch([text], return_tensors="pt", truncation=True)
    translated_tokens = model.generate(**tokenized)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text

def extract_text_from_pdf(uploaded_pdf):
    extracted_text = ""
    with pdfplumber.open(uploaded_pdf) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text(layout=True) + "\n"
    return extracted_text

def main():
    st.title("PDF Translator with Summarisation: English to Spanish")
    st.write("Upload a PDF document to extract, summarise and translate the text to Spanish.")

    uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        with st.spinner("Processing the file..."):
            model, tokenizer = load_translation_model()

            extracted_text = extract_text_from_pdf(uploaded_file)

            st.subheader("Extracted Text")
            st.write(extracted_text)

            cleaned_text = clean_text(extracted_text)

            summarization_pipeline = load_summarization_model()
            model, tokenizer = load_translation_model()

            st.write("### Summarising Text...")
            summarized_text = summarize_text(cleaned_text, summarization_pipeline)
            st.write("### Summarised Text:")
            st.text_area("Summarised Text", summarized_text, height=200)

            st.write("### Translating Text...")
            translated_text = translate_text(summarized_text, model, tokenizer)
            st.write("### Translated Text:")
            st.text_area("Translated Text", translated_text, height=200)

if __name__ == "__main__":
    main()