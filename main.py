from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from create_database import generate_data_store
from functions import predict


CHROMA_PATH = "chroma"


app = FastAPI(openapi_url="/openapi.json", docs_url="/docs")
llm = ChatOpenAI()
db = generate_data_store()
users = {}


class User:
    def __init__(self):
        self.llm = ChatOpenAI()


class ChatInput(BaseModel):
    Question: str


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, you can specify domains instead
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.post('/chat')
def chat(input_data: ChatInput):
    global db, previous_files, llm
 
    # llm = ChatOpenAI()
    response = predict(llm, input_data.Question, db)

    return {"response": response}


if __name__ == '__main__':
    import uvicorn
    # uvicorn.run(app, host='0.0.0.0', port=8765)
    uvicorn.run(app, port=8765)
