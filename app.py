import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import time

load_dotenv()

# Configure page
st.set_page_config(
    page_title="Interview Q&A Chatbot",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .answer-container {
        background-color: #f8f9fa;
        border-left: 4px solid #28a745;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .context-container {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        font-size: 0.9rem;
    }
    
    .success-message {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .error-message {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .question-input {
        font-size: 1.1rem;
        padding: 0.75rem;
    }
</style>
""", unsafe_allow_html=True)

## load the GROQ And OpenAI API KEY
groq_api_key = os.getenv('GROQ_API_KEY')
google_api_key = os.getenv("GOOGLE_API_KEY")

# Validate API keys
if not groq_api_key:
    st.error("🔑 GROQ_API_KEY not found in environment variables")
if not google_api_key:
    st.error("🔑 GOOGLE_API_KEY not found in environment variables")

os.environ["GOOGLE_API_KEY"] = google_api_key

# Header
st.markdown("""
<div class="main-header">
    <h1>🎯 Interview Preparation Q&A Chatbot</h1>
    <p>Get instant answers for DBMS, HR, OOPS, OS, and SQL topics</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for status and information
with st.sidebar:
    st.header("📊 System Status")
    
    # API Keys Status
    st.subheader("🔐 API Keys")
    if groq_api_key:
        st.success("✅ GROQ API Key")
    else:
        st.error("❌ GROQ API Key Missing")
    
    if google_api_key:
        st.success("✅ Google API Key")
    else:
        st.error("❌ Google API Key Missing")
    
    # Vector Database Status
    
    if "vectors" in st.session_state:
        st.success("✅ Vector Database Ready")
        if "docs" in st.session_state:
            st.info(f"📄 Documents: {len(st.session_state.docs)}")
        if "final_documents" in st.session_state:
            st.info(f"📝 Chunks: {len(st.session_state.final_documents)}")
    
    st.markdown("---")
    st.markdown("### 📚 Supported Topics")
    st.markdown("• Database Management Systems (DBMS)")
    st.markdown("• Human Resources (HR)")
    st.markdown("• Object-Oriented Programming (OOPS)")
    st.markdown("• Operating Systems (OS)")
    st.markdown("• Structured Query Language (SQL)")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

prompt = ChatPromptTemplate.from_template(
    """
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}
"""
)

def vector_embedding():
    if "vectors" not in st.session_state:
        try:
            with st.status("🔄 Initializing Vector Database...", expanded=True) as status:
                st.write("🚀 Initializing embeddings...")
                
                # Initialize embeddings with error handling
                st.session_state.embeddings = GoogleGenerativeAIEmbeddings(
                    model="models/embedding-001",
                    google_api_key=google_api_key
                )
                
                st.write("📁 Loading documents...")
                st.session_state.loader = PyPDFDirectoryLoader("./study_material")
                st.session_state.docs = st.session_state.loader.load()
                
                if not st.session_state.docs:
                    st.error("❌ No documents found in ./study_material directory")
                    return False
                
                st.write(f"✅ Found {len(st.session_state.docs)} documents")
                
                st.write("✂️ Splitting documents...")
                st.session_state.text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000, 
                    chunk_overlap=200
                )
                st.session_state.final_documents = st.session_state.text_splitter.split_documents(
                    st.session_state.docs[:20]
                )
                
                st.write(f"📝 Created {len(st.session_state.final_documents)} document chunks")
                
                st.write("🧠 Creating vector embeddings...")
                
                # Process documents in smaller batches to avoid rate limits
                batch_size = 5
                progress_bar = st.progress(0)
                
                for i in range(0, len(st.session_state.final_documents), batch_size):
                    batch = st.session_state.final_documents[i:i + batch_size]
                    batch_num = i//batch_size + 1
                    total_batches = (len(st.session_state.final_documents) + batch_size - 1)//batch_size
                    
                    st.write(f"⚡ Processing batch {batch_num}/{total_batches}")
                    progress_bar.progress(batch_num / total_batches)
                    
                    try:
                        if i == 0:
                            # Create initial FAISS index with first batch
                            st.session_state.vectors = FAISS.from_documents(batch, st.session_state.embeddings)
                        else:
                            # Add subsequent batches to existing index
                            batch_vectors = FAISS.from_documents(batch, st.session_state.embeddings)
                            st.session_state.vectors.merge_from(batch_vectors)
                        
                        # Add delay to avoid rate limiting
                        time.sleep(1)
                        
                    except Exception as e:
                        st.error(f"❌ Error processing batch {batch_num}: {str(e)}")
                        # Try with longer delay
                        time.sleep(5)
                        continue
                
                progress_bar.progress(1.0)
                status.update(label="✅ Vector Database Ready!", state="complete")
            
            return True
            
        except Exception as e:
            st.error(f"❌ Error in vector embedding: {str(e)}")
            if "quota" in str(e).lower() or "rate" in str(e).lower():
                st.error("⚠️ API quota or rate limit exceeded. Please try again later or check your Google API quota.")
            elif "api key" in str(e).lower():
                st.error("🔑 Invalid API key. Please check your GOOGLE_API_KEY in the .env file.")
            else:
                st.error("🌐 Please check your internet connection and API key validity.")
            return False
    
    return True

# Alternative embedding function using a different approach
def vector_embedding_alternative():
    """Alternative approach using sentence transformers if Google API fails"""
    if "vectors" not in st.session_state:
        try:
            with st.status("🔄 Trying Alternative Embedding Method...", expanded=True) as status:
                st.write("🔀 Using HuggingFace embeddings as backup...")
                
                # You can use HuggingFace embeddings as backup
                from langchain_community.embeddings import HuggingFaceEmbeddings
                
                st.session_state.embeddings = HuggingFaceEmbeddings(
                    model_name="sentence-transformers/all-MiniLM-L6-v2"
                )
                
                st.session_state.loader = PyPDFDirectoryLoader("./study_material")
                st.session_state.docs = st.session_state.loader.load()
                
                st.session_state.text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000, 
                    chunk_overlap=200
                )
                st.session_state.final_documents = st.session_state.text_splitter.split_documents(
                    st.session_state.docs[:20]
                )
                
                st.session_state.vectors = FAISS.from_documents(
                    st.session_state.final_documents, 
                    st.session_state.embeddings
                )
                
                status.update(label="✅ Alternative Vector Database Ready!", state="complete")
            
            return True
            
        except Exception as e:
            st.error(f"❌ Alternative embedding also failed: {str(e)}")
            return False

# Main interface
col1, col2 = st.columns([3, 1])

with col1:
    prompt1 = st.text_input(
        "💬 Ask your question about DBMS, HR, OOPS, OS, or SQL:",
        placeholder="e.g., What is normalization in DBMS?",
        help="Enter your interview preparation question here"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)  # Add spacing
    embed_button = st.button("🚀 Initialize Database", use_container_width=True)

if embed_button:
    success = vector_embedding()
    if success:
        st.markdown("""
        <div class="success-message">
            <h4>🎉 Success!</h4>
            <p>Vector Store Database is ready for questions!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="error-message">
            <h4>❌ Failed to Initialize</h4>
            <p>Failed to create vector embeddings. Try the alternative method below.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 Try Alternative Embedding", use_container_width=True):
            alt_success = vector_embedding_alternative()
            if alt_success:
                st.markdown("""
                <div class="success-message">
                    <h4>🎉 Alternative Method Success!</h4>
                    <p>Alternative Vector Store Database is ready!</p>
                </div>
                """, unsafe_allow_html=True)

# Only process the question if vectors have been initialized
if prompt1:
    if "vectors" in st.session_state:
        try:
            with st.spinner('🤔 Thinking... Please wait'):
                document_chain = create_stuff_documents_chain(llm, prompt)
                retriever = st.session_state.vectors.as_retriever()
                retrieval_chain = create_retrieval_chain(retriever, document_chain)
                
                start = time.process_time()
                response = retrieval_chain.invoke({'input': prompt1})
                response_time = time.process_time() - start
            
            # Display the answer with improved formatting
            st.markdown("### 💡 Answer")
            st.markdown(f"""
            <div class="answer-container">
                <h4>🎯 Response to: "{prompt1}"</h4>
                <p style="font-size: 1.1rem; line-height: 1.6;">{response['answer']}</p>
                <small style="color: #6c757d;">⏱️ Response generated in {response_time:.2f} seconds</small>
            </div>
            """, unsafe_allow_html=True)
            
            # Document similarity search with better formatting
            st.markdown("### 📚 Source References")
            with st.expander("🔍 View Document Similarity Search Results", expanded=False):
                if response.get("context"):
                    for i, doc in enumerate(response["context"], 1):
                        st.markdown(f"""
                        <div class="context-container">
                            <h5>📄 Reference {i}</h5>
                            <p style="font-size: 0.95rem; line-height: 1.5;">{doc.page_content}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("🔍 No specific document references found for this query.")
                    
        except Exception as e:
            st.markdown(f"""
            <div class="error-message">
                <h4>❌ Error Processing Question</h4>
                <p>Error: {str(e)}</p>
                <p>Please try again or check your input.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="info-box">
            <h4>⚠️ Database Not Ready</h4>
            <p>Please click the <strong>'🚀 Initialize Database'</strong> button first to set up the vector database before asking questions.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer with additional information
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6c757d; padding: 1rem;">
    <p>🎯 <strong>Interview Q&A Chatbot</strong> | Powered by LangChain & Streamlit</p>
    <p>💡 <em>Get comprehensive answers for your technical interview preparation</em></p>
</div>
""", unsafe_allow_html=True)