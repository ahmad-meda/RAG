import streamlit as st
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import Settings, VectorStoreIndex, get_response_synthesizer
from llama_index.readers.file import PyMuPDFReader
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API key from .env file
groq_api_key = os.getenv("GROQ_API_KEY")

# Configure settings
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
Settings.llm = Groq(model="llama3-8b-8192", api_key=groq_api_key)

st.title("Q/A Chatbot!")  

# File Upload with user-defined name
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.text("PDF File Uploaded Successfully!")
    
    # Save the uploaded file to a temporary location
    temp_file_path = os.path.join("temp.pdf")
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.read())
    
    # PDF Processing (using PyMuPDFReader)
    loader = PyMuPDFReader()
    documents = loader.load(temp_file_path)
    
    # Split Texts
    text_splitter = SentenceSplitter(chunk_size=1024)
    nodes = text_splitter.get_nodes_from_documents(documents)

    # Create vector index
    vector_index = VectorStoreIndex(nodes)
    
    # Initialize retrievers and query engine
    retriever = vector_index.as_retriever(similarity_top_k=10)
    query_engine = RetrieverQueryEngine(retriever=retriever, response_synthesizer=get_response_synthesizer())

    # Get User Question
    user_question = st.text_input("Ask a Question:")

    if st.button("Get Answer"):
        if user_question:
            # Get Response
            response = query_engine.query(user_question)

            # Display Answer
            st.subheader("Answer:")
            st.write(str(response))

            # Retrieve and display the chunks used for the answer
            source_nodes = response.source_nodes  # Access source nodes from response
            
            st.subheader("Chunks used:")
            for node in source_nodes:
                st.write(f"- {node.text}")
        else:
            st.warning("Please enter a question.")