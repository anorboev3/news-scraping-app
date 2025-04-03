from dotenv import load_dotenv
import os
import chromadb
from langchain.vectorstores import Chroma
from langchain_openai import AzureOpenAIEmbeddings

# Load environment variables from .env file
load_dotenv()

# Retrieve env data from environment variables
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
subscription_key = os.getenv("AZURE_OPENAI_KEY")
embeddings_api_version = os.getenv("EMBEDDINGS_API_VERSION")
embeddings_model_name = os.getenv("EMBEDDINGS_MODEL_NAME")

# Create an embedding function to pass into from_texts
# Initialize the embedding function using Azure OpenAI
embeddings = AzureOpenAIEmbeddings(
    model=embeddings_model_name,
    openai_api_version=embeddings_api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key
)

# Initialize the vector database
vector_db = None

PERSIST_DIRECTORY = os.path.join(os.getcwd(), "chroma_db")

# Function to store data in a vector database
# Takes a list of articles, extracts their content and metadata, and stores them in the vector database
# Initializes or clears the vector database as needed
def setup_vector_database(articles):
    texts = []
    metadatas = []

    for article in articles:
        texts.append(article['content'])
        metadatas.append({
            "url": article['url'],
            "headline": article['headline'],
            "summary": article['summary']
        })

    # Create persistence directory
    PERSIST_DIRECTORY = os.path.join(os.getcwd(), "chroma_db")
    os.makedirs(PERSIST_DIRECTORY, exist_ok=True)
    
    # Initialize ChromaDB client with the current approach
    client = chromadb.PersistentClient(path=PERSIST_DIRECTORY)
    
    # Use a consistent collection name
    collection_name = "news_articles"
    
    # Clear existing collection if it exists
    try:
        client.delete_collection(collection_name)
    except:
        pass
    
    # Create a new collection
    global vector_db
    
    vector_db = Chroma.from_texts(
        texts=texts, 
        embedding=embeddings, 
        metadatas=metadatas,
        collection_name=collection_name,
        client=client
    )

# Function to perform semantic search
def search_query(query):
    if vector_db is None:
        return "Vector database is empty. Please process URLs first."

    results = vector_db.similarity_search_with_score(query)

    # Filter results based on a similarity score threshold
    threshold = 0.5  # Adjust this value as needed
    filtered_results = [(result, score) for result, score in results if score <= threshold]

    if filtered_results:
        output = []
        for result, score in filtered_results:
            output.append({
                "headline": result.metadata['headline'],
                "summary": result.metadata['summary'],
                "url": result.metadata['url'],
                "similarity_score": score
            })
        return output
    else:
        return "No matching results found with a good similarity score."