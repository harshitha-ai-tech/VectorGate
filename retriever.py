from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load embeddings and vectorstore
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings=embeddings,
    allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever()

def retrieve_answer(user_question: str):
    results = retriever.get_relevant_documents(user_question)
    if not results:
        return "Sorry, I don't know the answer."

    full_answer = " ".join([doc.page_content for doc in results])
    short_answer = full_answer.split(". ")[0] + "."

    if "detail" in user_question.lower() or "more" in user_question.lower():
        return full_answer
    return short_answer
