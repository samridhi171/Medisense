import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import os

# Set the API key directly here and change this according to your API
api_key = "AIzaSyArJVsC_iaUDJqOCUsRTa3QwYheNgoTTaI"

from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_pdf_path, output_pdf_path, start_page, end_page):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Adjusting for 0-based indexing
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])

    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)

# Example usage
input_pdf_path = "Harrison's Principles of Internal Medicine, 20th Edition 2020.pdf"
pdf_paths = "Harrison's_Extracted_Pages.pdf"
start_page = 100  # Start from the first page
end_page = 700  # Extract up to the 500th page

extract_pages(input_pdf_path, pdf_paths, start_page, end_page)


# Set PDF file paths directly here and change it accordingly
pdf_paths = [r"Harrison's_Extracted_Pages.pdf"]

# Set page configuration
st.set_page_config(page_title="Medical Bot", layout="wide")

# Apply gradient background using custom CSS for main content and enhance fonts
page_bg_gradient = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

    .stApp {
        background: linear-gradient(135deg, #FFFFFF, #CEE1F8);
        font-family: 'Roboto', sans-serif;
        display: flex;
        justify-content: flex-start; /* Align content to the left */
        padding: 20px;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Roboto', sans-serif;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 20px;
        color: #000A8E; /* Deep blue for headings and subheadings */
    }

    .stMarkdown p {
        font-family: 'Roboto', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        text-align: left; /* Align text to the left */
    }

    .stButton>button {
        font-family: 'Roboto', sans-serif;
        font-weight: 600;
        letter-spacing: 0.5px;
        border-radius: 25px;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #007BFF;
        color: white;
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.4);
    }

    .stTextInput > div > input {
        border-radius: 25px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        border: 1px solid #CED4DA;
        transition: border-color 0.3s ease;
    }

    .stTextInput > div > input:focus {
        border-color: #007BFF;
        outline: none;
    }

    .icon {
        margin-right: 10px;
        font-size: 20px;
    }

    .icon-upload { color: #007BFF; }
    .icon-processing { color: #FFC107; }
    .icon-question { color: #28A745; }
</style>
"""
st.markdown(page_bg_gradient, unsafe_allow_html=True)

# Add the MediSense icon at the top left
st.image("MediSenseLogo.png", width=80)

st.markdown("""
## Dr. Pulse: Your Digital Health Assistant
This AI-powered chatbot helps you quickly find the health information you need from your uploaded PDF documents.
            """, unsafe_allow_html=True)

st.image("cute-doctor-robot-holding-clipboard-stethoscope-cartoon-vector-icon-illustration-science-techno (1).png", width=350)

st.markdown("""
### How It Works

1. <i class="fas fa-file-upload icon icon-upload"></i> Upload Your Documents: Just upload your PDF files.
2. <i class="fas fa-cogs icon icon-processing"></i> Processing: The system quickly processes the documents for you.
3. <i class="fas fa-question-circle icon icon-question"></i> Ask a Question: Type in your question, and Dr. Pulse will provide answers based on the content of your documents.
""", unsafe_allow_html=True)

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks, api_key):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain(api_key):
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, google_api_key=api_key)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question, api_key):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain(api_key)
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    print("Chatbot Response:", response["output_text"])
    return response["output_text"]

def main():
    

    st.header("Your AI Assistant🩺")

    user_question = st.text_input("Need quick health insights? Just ask Dr. Pulse below.", key="user_question")

    if st.button("Submit", key="submit_button"):  # Submit button for the question
        if user_question:  # Ensure user question is provided
            response = user_input(user_question, api_key)
            st.write("Reply: ", response)  # Display response in Streamlit interface

    with st.sidebar:
        st.title("Menu:")
        if st.button("Submit & Process", key="process_button"):  # Process documents when button is clicked
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_paths)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks, api_key)
                st.success("Done")

if __name__ == "__main__":
    main()
