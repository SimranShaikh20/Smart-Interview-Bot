# Interview Preparation Q&A Chatbot

## Project Overview
The **Interview Preparation Q&A Chatbot** is a powerful Streamlit-based application designed to assist with interview preparation by providing concise and accurate answers to user queries based on context extracted from provided study materials. This application leverages advanced large language models (LLMs) and embeddings to enable document-based question-answering. It is specifically tailored for interview preparation on subjects like DBMS, SQL, HR, OS, and related topics.


**Application Link**: [Interview Preparation Q&A Chatbot](https://smartinterviewbot-cvoxuk5tmbznytsp6frhdy.streamlit.app/)



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

## Project Workflow
1. **Setup**:
   - Load API keys from environment variables (`GROQ_API_KEY` and `GOOGLE_API_KEY`).
   - Initialize the ChatGroq model and prompt template for accurate and context-driven responses.

2. **Document Loading**:
   - Load PDF documents from the `./study_material` directory.
   - Split documents into overlapping chunks for better retrieval performance.

3. **Embedding and Retrieval**:
   - Use Google Generative AI Embeddings to create vector representations of document chunks.
   - Store these vectors in a FAISS vector database for efficient similarity searching.

4. **Question Answering**:
   - Retrieve relevant document chunks based on the user's query.
   - Use the ChatGroq model to generate answers based on retrieved context.
   - Display results and relevant document excerpts in the Streamlit interface.

## How to Run the Application
1. **Install Dependencies**:
   Ensure the following libraries are installed:
   ```bash
   pip install streamlit langchain_groq langchain langchain-core langchain-community faiss-cpu dotenv
   ```

2. **Set Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add the following keys:
     ```env
     GROQ_API_KEY=your_groq_api_key_here
     GOOGLE_API_KEY=your_google_api_key_here
     ```

3. **Prepare Study Materials**:
   - Place relevant PDF files in the `./study_material` directory.

4. **Run the Application**:
   - Launch the Streamlit application:
     ```bash
     streamlit run app.py
     ```

5. **Interact with the App**:
   - Use the input box to enter questions on topics like DBMS, HR, OOPS, OS, or SQL.
   - Click the **Documents Embedding** button to prepare the vector store.
   - View detailed results and document context in the interface.

## Use Cases
- **Interview Preparation**: Gain quick and precise answers to common interview topics.
- **Document Insights**: Extract knowledge from study materials effectively.
- **Contextual Understanding**: Retrieve document chunks relevant to specific queries.

## Dependencies
- **Streamlit**: Interactive user interface.
- **LangChain**: Enables Q&A chains and document retrieval.
- **ChatGroq**: Provides LLM capabilities.
- **FAISS**: Efficient vector similarity search.
- **Google Generative AI Embeddings**: Generates embeddings for text data.
- **PyPDFDirectoryLoader**: Loads and processes PDF documents.

## Future Enhancements
- Add support for more file types (e.g., Word, Excel).
- Implement multi-language support for non-English documents.
- Integrate more powerful LLMs or domain-specific models.
- Optimize the user interface for better interaction and aesthetics.

## Directory Structure
```plaintext
.
├── app.py                     # Main application script
├── study_material/            # Directory containing study materials (PDFs)
├── .env                       # Environment variables file
└── requirements.txt           # Dependencies list
```


## Author
**Simran Shaikh**
