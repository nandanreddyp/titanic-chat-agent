from fastapi import FastAPI
from pydantic import BaseModel
from .agent import create_agent

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

app = FastAPI()
agent = create_agent()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(request: QueryRequest):
    response = agent.run(request.question)
    return {"answer": response}
