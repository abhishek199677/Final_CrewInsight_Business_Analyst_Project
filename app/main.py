from fastapi import FastAPI, Depends, HTTPException, Header
from app.models import MarketRequest, SummaryResponse
from app.orchestrator import AgentOrchestrator
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = "crewinsight-key"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/")
def read_root():
    return {"message": "Welcome to CrewInsight API. Use the /analyze endpoint to analyze market data."}


@app.post("/analyze", response_model=SummaryResponse, dependencies=[Depends(verify_api_key)])
def analyze(request: MarketRequest):
    result = AgentOrchestrator().run_pipeline(request)
    return result


@app.get("/")
def home():
    return {
        "message": "✅ Welcome to CrewInsight - Business Analyst Agent API!",
        "usage": "Go to /docs to test the API or use the /analyze endpoint with a POST request."
    }
