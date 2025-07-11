from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.responses import HTMLResponse
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


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>CrewInsight API</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>✅ Welcome to CrewInsight - Business Analyst Agent</h1>
            <p>Visit the <a href='/docs'>Swagger UI</a> to test the API.</p>
            <p>Or use the <code>/analyze</code> endpoint with your market query.</p>
        </body>
    </html>
    """


@app.post("/analyze", response_model=SummaryResponse, dependencies=[Depends(verify_api_key)])
def analyze(request: MarketRequest):
    result = AgentOrchestrator().run_pipeline(request)
    return result
