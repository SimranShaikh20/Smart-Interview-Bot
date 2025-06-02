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

## load the GROQ And OpenAI API KEY
groq_api_key = os.getenv('GROQ_API_KEY')
google_api_key = os.getenv("GOOGLE_API_KEY")

# Validate API keys
if not groq_api_key:
    st.error("GROQ_API_KEY not found in environment variables")
if not google_api_key:
    st.error("GOOGLE_API_KEY not found in environment variables")

os.environ["GOOGLE_API_KEY"] = google_api_key

st.title("Interview Preparation Q&A Chatbot")

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
            st.write("Initializing embeddings...")
            
            # Initialize embeddings with error handling
            st.session_state.embeddings = GoogleGenerativeAIEmbeddings(
                model="models/embedding-001",
                google_api_key=google_api_key
            )
            
            st.write("Loading documents...")
            st.session_state.loader = PyPDFDirectoryLoader("./study_material")
            st.session_state.docs = st.session_state.loader.load()
            
            if not st.session_state.docs:
                st.error("No documents found in ./study_material directory")
                return False
            
            st.write(f"Found {len(st.session_state.docs)} documents")
            
            st.write("Splitting documents...")
            st.session_state.text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000, 
                chunk_overlap=200
            )
            st.session_state.final_documents = st.session_state.text_splitter.split_documents(
                st.session_state.docs[:20]
            )
            
            st.write(f"Created {len(st.session_state.final_documents)} document chunks")
            
            st.write("Creating vector embeddings... This may take a moment.")
            
            # Process documents in smaller batches to avoid rate limits
            batch_size = 5
            all_vectors = []
            
            for i in range(0, len(st.session_state.final_documents), batch_size):
                batch = st.session_state.final_documents[i:i + batch_size]
                st.write(f"Processing batch {i//batch_size + 1}/{(len(st.session_state.final_documents) + batch_size - 1)//batch_size}")
                
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
                    st.error(f"Error processing batch {i//batch_size + 1}: {str(e)}")
                    # Try with longer delay
                    time.sleep(5)
                    continue
            
            return True
            
        except Exception as e:
            st.error(f"Error in vector embedding: {str(e)}")
            if "quota" in str(e).lower() or "rate" in str(e).lower():
                st.error("API quota or rate limit exceeded. Please try again later or check your Google API quota.")
            elif "api key" in str(e).lower():
                st.error("Invalid API key. Please check your GOOGLE_API_KEY in the .env file.")
            else:
                st.error("Please check your internet connection and API key validity.")
            return False
    
    return True

# Alternative embedding function using a different approach
def vector_embedding_alternative():
    """Alternative approach using sentence transformers if Google API fails"""
    if "vectors" not in st.session_state:
        try:
            st.write("Trying alternative embedding method...")
            
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
            
            return True
            
        except Exception as e:
            st.error(f"Alternative embedding also failed: {str(e)}")
            return False

prompt1 = st.text_input("Enter Your Question for Topics(DBMS,HR,OOPS,OS,SQL)")

if st.button("Documents Embedding"):
    success = vector_embedding()
    if success:
        st.success("Vector Store DB Is Ready")
    else:
        st.error("Failed to create vector embeddings. Trying alternative method...")
        if st.button("Try Alternative Embedding"):
            alt_success = vector_embedding_alternative()
            if alt_success:
                st.success("Alternative Vector Store DB Is Ready")

# Only process the question if vectors have been initialized
if prompt1:
    if "vectors" in st.session_state:
        try:
            document_chain = create_stuff_documents_chain(llm, prompt)
            retriever = st.session_state.vectors.as_retriever()
            retrieval_chain = create_retrieval_chain(retriever, document_chain)
            
            start = time.process_time()
            response = retrieval_chain.invoke({'input': prompt1})
            print("Response time :", time.process_time() - start)
            
            st.write(response['answer'])
            
            # With a streamlit expander
            with st.expander("Document Similarity Search"):
                # Find the relevant chunks
                for i, doc in enumerate(response["context"]):
                    st.write(doc.page_content)
                    st.write("--------------------------------")
                    
        except Exception as e:
            st.error(f"Error processing question: {str(e)}")
    else:
        st.warning("Please click 'Documents Embedding' button first to initialize the vector database.")

# Debug information
with st.expander("Debug Information"):
    st.write("Environment Variables Status:")
    st.write(f"GROQ_API_KEY: {'✓ Set' if groq_api_key else '✗ Missing'}")
    st.write(f"GOOGLE_API_KEY: {'✓ Set' if google_api_key else '✗ Missing'}")
    
    if "docs" in st.session_state:
        st.write(f"Documents loaded: {len(st.session_state.docs)}")
    if "final_documents" in st.session_state:
        st.write(f"Document chunks: {len(st.session_state.final_documents)}")
    if "vectors" in st.session_state:
        st.write("✓ Vector database initialized")