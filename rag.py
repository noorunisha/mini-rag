from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

# 1. Load knowledge
loader = TextLoader("knowledge.txt")
documents = loader.load()

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.split_documents(documents)

print("Number of chunks:", len(chunks))

# 3. Create LOCAL embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Store embeddings in FAISS
vectorstore = FAISS.from_documents(chunks, embeddings)

# 5. Ask a question
question = input("\nAsk something: ")

# 6. Retrieve relevant information
results = vectorstore.similarity_search(question, k=2)

context = "\n\n".join(
    doc.page_content for doc in results
)

print("\nRetrieved information:")
print(context)

# 7. Use LOCAL Ollama LLM
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

# 8. Give retrieved context to the LLM
prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer clearly and simply.
"""

response = llm.invoke(prompt)

# 9. Show answer
print("\nAnswer:")
print(response.content)