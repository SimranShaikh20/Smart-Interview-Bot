# 🚀 Interview Preparation Q&A Chatbot

## 📌 Project Overview
The **Interview Preparation Q&A Chatbot** is a powerful **Streamlit-based** application designed to assist with interview preparation by providing **concise and accurate answers** to user queries based on study materials. This application leverages **Large Language Models (LLMs)** and **embeddings** to enable **document-based question-answering** for subjects like **DBMS, SQL, HR, OS, and more**.

## ✨ Features
### 📝 Document Ingestion
- Loads documents from a specified directory containing **PDF files**.
- Automatically splits documents into **smaller, manageable chunks** using a recursive text splitter for efficient processing.

### 🔍 Vector Store Creation
- Embeds document chunks using **Google Generative AI Embeddings**.
- Builds a **FAISS (Facebook AI Similarity Search) vector database** for efficient similarity searches.

### 💡 Contextual Q&A
- Uses the **ChatGroq LLM (Llama3-8b-8192)** to answer questions.
- Employs a retriever to fetch **relevant document chunks** for context-based Q&A.

### 🎭 Interactive Interface
- Simple and user-friendly **Streamlit UI**.
- Provides an **input box** for user queries.
- Allows users to **upload documents** for Q&A by clicking a button.
- Displays retrieved **document context and similarity matches** in an expandable section.

### ⏱️ Performance Metrics
- Tracks and displays **response times** for Q&A tasks.

## ⚙️ How the Project Works
### 🎨 User Interface (Streamlit)
The chatbot is built using **Streamlit**, allowing users to interact via an intuitive web interface where they can input their questions related to interview preparation.

### 📥 Input Processing
When a user enters a query, the system processes the input to understand the **context and intent** of the question.

### 🧠 Embedding Generation
- The user's query is converted into a **vector embedding** using **Google AI embeddings**.
- Embeddings capture **semantic meaning**, allowing for accurate retrieval of relevant information.

### 📚 Vector Database (FAISS)
- **FAISS** is used for **efficient similarity search and clustering** of dense vectors.
- Interview-related data is stored in a **vectorized form** in the FAISS database for **fast and precise retrieval**.

### 🔎 Similarity Search
- The system performs a **similarity search** in the FAISS database to find the most relevant documents or answers.
- **FAISS compares** the query embedding with stored embeddings to **retrieve the closest matches**.

### 🤖 Response Generation (ChatGroq LLM)
- The retrieved data is passed to **ChatGroq LLM**, which processes the information and generates a **tailored, human-like response**.
- The **LLM ensures contextually appropriate and clear answers**.

### 📤 Output to User
- The generated response is **displayed** to the user in the **Streamlit interface**.
- Users receive **concise, accurate, and contextually relevant** answers.

## 🔮 Future Enhancements
- 🏗️ **Support for more file types** (Word, Excel, etc.)
- 🌍 **Multi-language support** for non-English documents
- 🚀 **Integration with more powerful LLMs**
- 🎨 **Optimized UI** for better interaction and aesthetics

## 📂 Installation & Setup
### Prerequisites
- Python 3.8+
- Pip
- Virtual environment (optional but recommended)

### 🛠️ Setup Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/SimranShaikh20/Smart-Interview-Bot.git
   cd Smart-Interview-Bot
   ```
2. **Create and activate a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

## 🤝 Contributing
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

## 👨‍💻 Author
**Simran Shaikh**

## 📜 License
This project is licensed under the **MIT License**.

🚀 **Happy Coding & Good Luck with Your Interviews!** 💡🎯