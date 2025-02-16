## Interview Preparation Q&A Chatbot

### Project Overview
The **Interview Preparation Q&A Chatbot** is a powerful Streamlit-based application designed to assist with interview preparation by providing concise and accurate answers to user queries based on context extracted from provided study materials. This application leverages advanced large language models (LLMs) and embeddings to enable document-based question-answering. It is specifically tailored for interview preparation on subjects like DBMS, SQL, HR, OS, and related topics.

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

## How Data is Fetched from the Vector Database

### Data Preparation:
The project involves pre-processing a large dataset of interview-related content (e.g., PDFs, text files) into vector embeddings using Google AI embeddings.

These embeddings are then indexed and stored in the FAISS vector database.

### User Query Handling:
When a user enters a query, the system converts the query into a vector embedding using the same embedding model.

### Search in FAISS:
The system performs a k-nearest neighbors (k-NN) search in the FAISS database to find the most similar vectors to the user's query.

FAISS efficiently retrieves the top-k most relevant documents or answers based on the similarity score.

### Contextual Retrieval:
The retrieved data is passed to the ChatGroq LLM, which uses the context to generate a coherent and accurate response.

## Key Technologies Used
- **Streamlit**: For building the user interface and chatbot.
- **Google AI Embeddings**: For converting text into vector representations.
- **FAISS**: For efficient storage and retrieval of vectorized data.
- **ChatGroq LLM**: For generating contextually appropriate and human-like responses.
- **PDF Processing**: For extracting and processing interview-related content from PDFs.

## Benefits of the Project
- **Efficient Retrieval**: FAISS ensures fast and accurate retrieval of relevant information.
- **Context-Aware Responses**: The use of embeddings and LLMs ensures that answers are tailored to the user's query.
- **User-Friendly Interface**: Streamlit provides an intuitive and easy-to-use interface for users.
- **Scalability**: The system can handle large datasets and multiple users simultaneously.

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

## Directory Structure
```plaintext
.
├── app.py                     # Main application script
├── study_material/            # Directory containing study materials (PDFs)
├── .env                       # Environment variables file
└── requirements.txt           # Dependencies list
```

## Future Enhancements
- Add support for more file types (e.g., Word, Excel).
- Implement multi-language support for non-English documents.
- Integrate more powerful LLMs or domain-specific models.
- Optimize the user interface for better interaction and aesthetics.

## Author
**Simran Shaikh**
