from fastapi import FastAPI
from pydantic import BaseModel

from main import run

app = FastAPI(
    title="AI RAG Agent",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    query: str
    
@app.post("/query")
def query(request: QueryRequest):

    answer = run(request.query)

    return {
        "answer": answer,
        "sources": []
    }
    

