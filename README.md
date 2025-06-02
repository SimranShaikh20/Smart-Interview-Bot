# 🎯 Enhanced Interview Preparation Q&A Chatbot

<p>
  <img src="https://img.shields.io/badge/Prompt%20Engineering-800080?logo=openai&logoColor=white" alt="Prompt Engineering" />
  <img src="https://img.shields.io/badge/LangChain-0F4C81?logo=langchain&logoColor=white" alt="LangChain" />
  <img src="https://img.shields.io/badge/RAG-FF6F61?logo=semanticweb&logoColor=white" alt="RAG (Retrieval-Augmented Generation)" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/FAISS-4285F4?logo=meta&logoColor=white" alt="FAISS" />
  <img src="https://img.shields.io/badge/Google%20AI-4285F4?logo=google&logoColor=white" alt="Google AI" />
</p>

---

## 📌 Project Overview

The **Enhanced Interview Preparation Q&A Chatbot** is a sophisticated **Streamlit-based application** with a modern, professional UI designed to help users excel in technical interviews. It leverages **Large Language Models (LLMs)** and **advanced embeddings** to provide context-aware answers based on uploaded study materials. The chatbot specializes in **DBMS, SQL, HR, OOPS, OS** topics with an intuitive and visually appealing interface.

---

## 🚀 Live Demo

🔗 [Click Here to Try the Enhanced Chatbot](https://smart-interview-bot.streamlit.app/)

---

## ✨ Key Features

### 🎨 **Modern UI/UX**
- **Professional gradient design** with custom CSS styling
- **Responsive sidebar** with real-time system status monitoring
- **Interactive progress indicators** and loading animations
- **Card-based layout** for better content organization
- **Status dashboard** with API key validation and database metrics

### 📝 **Advanced Document Processing**
- Loads **PDF documents** from specified directory with batch processing
- **Intelligent text splitting** using RecursiveCharacterTextSplitter
- **Rate limit handling** with automatic retry mechanisms
- **Alternative embedding fallback** using HuggingFace transformers

### 🔍 **Smart Vector Store Management**
- **Google Generative AI Embeddings** with `models/embedding-001`
- **FAISS vector database** for efficient similarity search
- **Batch processing** to handle API rate limits gracefully
- **Memory-efficient indexing** with merge capabilities

### 💡 **Intelligent Q&A System**
- **ChatGroq LLM (Llama3-8b-8192)** for high-quality responses
- **RAG (Retrieval-Augmented Generation)** for context-aware answers
- **Dynamic context retrieval** with similarity scoring
- **Response time tracking** for performance optimization

### 🛡️ **Robust Error Handling**
- **API key validation** with clear status indicators
- **Fallback embedding methods** for reliability
- **Graceful error recovery** with user-friendly messages
- **Rate limit management** with automatic retries

---

## ⚙️ How It Works

### 🎨 Enhanced Streamlit Interface
Users interact through a **modern, professional web interface** with gradient backgrounds, status indicators, and organized layouts.

### 📥 Intelligent Input Processing
User queries are processed with **semantic understanding** using Google AI embeddings, with fallback options for maximum reliability.

### 📚 Advanced FAISS Vector Store
Document chunks are stored as high-dimensional vectors with **batch processing** and **merge capabilities** for efficient similarity searches.

### 🔎 Enhanced RAG Implementation
The system uses **optimized Retrieval-Augmented Generation** with ChatGroq's Llama3 model, providing contextually rich and accurate responses.

### 📤 Professional Response Display
Answers are presented in **beautifully formatted containers** with source references, response times, and expandable context sections.

---

## 🔧 Technical Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit UI  │───▶│  Document Loader │───▶│ Text Splitter   │
│   (Enhanced)    │    │   (PDF Reader)   │    │ (Recursive)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        │
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Query    │◀───│   ChatGroq LLM   │◀───│ FAISS Retriever │
│   (Response)    │    │  (Llama3-8b)     │    │ (Similarity)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        ▲
                       ┌──────────────────┐    ┌─────────────────┐
                       │ Google AI        │───▶│ Vector Store    │
                       │ Embeddings       │    │ (FAISS Index)   │
                       └──────────────────┘    └─────────────────┘
```

---

## 📂 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment (recommended)
- API Keys (GROQ_API_KEY, GOOGLE_API_KEY)

### 🛠️ Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/SimranShaikh20/Smart-Interview-Bot.git
   cd Smart-Interview-Bot
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Create study materials directory**
   ```bash
   mkdir study_material
   # Add your PDF files to this directory
   ```

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## 📋 Requirements

```txt
streamlit>=1.28.0
langchain>=0.1.0
langchain-groq>=0.1.0
langchain-google-genai>=1.0.0
langchain-community>=0.0.20
faiss-cpu>=1.7.4
pypdf>=3.17.0
python-dotenv>=1.0.0

```

---

## 🔑 API Configuration

### GROQ API Key
1. Sign up at [GROQ Console](https://console.groq.com/)
2. Generate your API key
3. Add to `.env` file as `GROQ_API_KEY`

### Google AI API Key
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create and configure your API key
3. Add to `.env` file as `GOOGLE_API_KEY`

---

## 🚀 Usage Guide

1. **Initialize Database**: Click "🚀 Initialize Database" to process your PDF documents
2. **Monitor Status**: Check the sidebar for real-time system status
3. **Ask Questions**: Enter your interview questions in the input field
4. **View Results**: Get formatted answers with source references
5. **Explore Context**: Expand the similarity search section for detailed context

---

## 📊 Supported Topics

- 🗄️ **Database Management Systems (DBMS)**
- 💼 **Human Resources (HR)**
- 🧩 **Object-Oriented Programming (OOPS)**
- 💻 **Operating Systems (OS)**
- 🔍 **Structured Query Language (SQL)**

---

## 🔮 Future Enhancements

- 🏗️ **Multi-format support** (Word, Excel, PowerPoint)
- 🌍 **Multi-language capabilities** for global users
- 🤖 **Advanced LLM integration** (GPT-4, Claude)
- 📱 **Mobile-responsive design** optimization
- 🔊 **Voice interaction** capabilities
- 📈 **Analytics dashboard** for usage insights
- 🔐 **User authentication** and session management

---

## 🛠️ Troubleshooting

### Common Issues

**"API Key not found"**
- Ensure `.env` file exists with valid API keys
- Check environment variable names match exactly

**"No documents found"**
- Verify PDF files are in `./study_material/` directory
- Check file permissions and formats

**"Rate limit exceeded"**
- Wait and retry - the app handles this automatically
- Consider using the HuggingFace fallback option

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Simran Shaikh**
- GitHub: [@SimranShaikh20](https://github.com/SimranShaikh20)


---

## 🙏 Acknowledgments

- **LangChain** for the powerful RAG framework
- **Streamlit** for the amazing web app framework
- **GROQ** for lightning-fast LLM inference
- **Google AI** for advanced embedding models
- **FAISS** for efficient vector similarity search

---

## ⭐ Star History

If this project helped you, please consider giving it a ⭐!

---

🚀 **Happy Learning & Best of Luck with Your Interviews!** 💡🎯