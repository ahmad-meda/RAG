# RAG Model Chatbot

This is assignment contains 2 tasks,a Google collab notebook explaining the pipeline and implementing a Chatbot interface.

This application is implemented using python.The interface is hosted using Streamlit and containerized using Docker.

## Requirements

- Python 3.8+

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ahmad-meda/RAG
    cd jessup-cellars-chatbot
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Set up your environment variables**:
    Create a `.env` file in the project directory with the following content:
    ```sh
    GROQ_API_KEY=your_groq_api_key
    ```

## Install Docker

1. Clone the repository:
   ```git clone https://github.com/ahmad-meda/RAG.git```
   ```cd RAG```

2. Build the Docker image:
   ```docker build -t qa-chatbot .```

3. Run the Docker container:
   ```docker run -p 8501:8501 qa-chatbot```

4. Access the app at `http://localhost:8501`.

## Usage Instructions
1. **Upload a PDF File**: Click on the "Upload a PDF file" button to upload your document.
2. **Ask a Question**: Once the PDF is uploaded, type your question in the provided text input box.
3. **Get Answer**: Click the "Get Answer" button to receive a response based on the content of the uploaded PDF.
