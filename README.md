# Interview Preparation Q&A Chatbot 🚀

![Innovative Logo](images/innovative_logo.png)

## Project Overview
The **Interview Preparation Q&A Chatbot** is a powerful Streamlit-based application designed to assist with interview preparation by providing concise and accurate answers to user queries based on context extracted from provided study materials. This application leverages advanced large language models (LLMs) and embeddings to enable document-based question-answering. It is specifically tailored for interview preparation on subjects like DBMS, SQL, HR, OS, and related topics.

![Rocket Logo](images/rocket_logo.png)

## Features
1. **Document Ingestion**
   - Loads documents from a specified directory containing PDF files.
   - Automatically splits documents into smaller, manageable chunks using a recursive text splitter for effective processing.

2. **Vector Store Creation**
   - Embeds document chunks using **Google Generative AI Embeddings**.
   - Builds a FAISS (Facebook AI Similarity Search) vector database for efficient similarity searches.

3. **Contextual Q&A**
   - Uses the **ChatGroq** LLM (Llama3-8b-8192) to answer questions.
   - Employs a retriever to fetch the most relevant document chunks for context-based Q&A.

4. **Interactive Interface**
   - Simple and user-friendly Streamlit UI.
   - Provides an input box for user questions.
   - Allows users to embed documents for Q&A by clicking a button.
   - Displays retrieved document context and similarity matches in an expandable section.

5. **Performance Metrics**
   - Tracks and displays response times for Q&A tasks.

## How the Project Works

### User Interface (Streamlit):
The chatbot is built using Streamlit, a Python framework for creating web applications.
Users interact with the chatbot through an intuitive interface where they can input their questions related to interview preparation.

### Input Processing:
When a user enters a query, the system processes the input to understand the context and intent of the question.

### Embedding Generation:
The user's query is converted into a vector embedding using Google AI embeddings. Embeddings are numerical representations of text that capture semantic meaning, allowing the system to compare and retrieve relevant information.

### Vector Database (FAISS):
The project uses FAISS, a library for efficient similarity search and clustering of dense vectors, to store and retrieve pre-processed data.
The data (e.g., interview questions, answers, and related content) is stored in a vectorized form in the FAISS database. This allows for fast and accurate retrieval of relevant information based on the user's query.

### Similarity Search:
The system performs a similarity search in the FAISS database to find the most relevant documents or answers that match the user's query.
FAISS compares the vector embedding of the user's query with the embeddings of the stored data and retrieves the closest matches.

### Response Generation (ChatGroq LLM):
The retrieved data is passed to the ChatGroq LLM, a large language model, which processes the information and generates a tailored, human-like response.
The LLM ensures that the answer is contextually appropriate and easy to understand.

### Output to User:
The generated response is displayed to the user through the Streamlit interface, providing them with a clear and concise answer to their query.

## Future Enhancements
- Add support for more file types (e.g., Word, Excel).
- Implement multi-language support for non-English documents.
- Integrate more powerful LLMs or domain-specific models.
- Optimize the user interface for better interaction and aesthetics.

## Author
**Simran Shaikh**
