from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from data.knowledge import KNOWLEDGE_TEXT

def ingest_knowledge():
    documents = [Document(page_content=KNOWLEDGE_TEXT)]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("vectorstore")
    print("✅ Knowledge ingested successfully")

if __name__ == "__main__":
    ingest_knowledge()
