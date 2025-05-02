# 🚀 Interview Preparation Q&A Chatbot

<p>
  <img src="https://img.shields.io/badge/Prompt%20Engineering-800080?logo=openai&logoColor=white" alt="Prompt Engineering" />
  <img src="https://img.shields.io/badge/LangChain-0F4C81?logo=langchain&logoColor=white" alt="LangChain" />
  <img src="https://img.shields.io/badge/RAG-FF6F61?logo=semanticweb&logoColor=white" alt="RAG (Retrieval-Augmented Generation)" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
</p>

---

## 📌 Project Overview

The **Interview Preparation Q&A Chatbot** is a smart and efficient **Streamlit-based application** designed to help users prepare for interviews. It uses **Large Language Models (LLMs)** and **embeddings** to answer questions based on uploaded study materials. The chatbot supports subjects like **DBMS, SQL, HR, OS**, and more by enabling **context-aware document-based Q&A**.

---

## 🚀 Live Demo

🔗 [Click Here to Try the Chatbot](https://smart-interview-bot-b7pshyhw8syhmdzhf6q6mu.streamlit.app/)

---

## ✨ Features

### 📝 Document Ingestion
- Loads **PDF documents** from a specified folder.
- Splits text into **smaller, manageable chunks** using a recursive text splitter.

### 🔍 Vector Store Creation
- Converts text chunks to embeddings using **Google Generative AI Embeddings**.
- Stores them in a **FAISS vector database** for efficient retrieval.

### 💡 Contextual Q&A
- Uses **ChatGroq LLM (Llama3-8b-8192)** to answer questions.
- Retrieves **most relevant document chunks** for context-aware responses.

### 🎭 Interactive UI
- Built with **Streamlit** for ease of use.
- Users can **upload documents** and **enter queries**.
- Shows **retrieved context** and **similarity matches**.

### ⏱️ Performance Tracking
- Displays **response time** for each query to monitor efficiency.

---

## ⚙️ How It Works

### 🎨 Streamlit Interface
Users interact with the chatbot through a simple **web interface**, entering questions or uploading PDFs.

### 📥 Input Processing
User queries are transformed into **vector embeddings** using Google AI to understand their semantic meaning.

### 📚 FAISS Vector Store
Document chunks are stored as vectors. A **similarity search** finds the best-matching chunks for any query.

### 🔎 Retrieval + Generation (RAG)
The app uses **RAG (Retrieval-Augmented Generation)** to fetch relevant context and generate accurate, natural responses via **ChatGroq LLM**.

### 📤 Response Output
Answers are displayed back in the UI, along with expandable retrieved context sections.

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