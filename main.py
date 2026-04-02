from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from retriever import retrieve_answer

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.websocket("/ws/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            user_msg = data.get("message", "")
            answer = retrieve_answer(user_msg)
            await websocket.send_json({"reply": answer})
    except WebSocketDisconnect:
        print("Client disconnected")

@app.get("/")
async def get():
    return {"message": "RAG Chatbot running! Visit /static/index.html"}
