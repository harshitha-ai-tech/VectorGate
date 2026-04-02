import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def generate_answer(context, question):

    prompt = f"""
YYou are a friendly chatbot.
Answer like a human, not a textbook.
Be concise, clear, and conversational.
If the answer is long, summarize it.
Do NOT repeat unnecessary details.
".

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content
