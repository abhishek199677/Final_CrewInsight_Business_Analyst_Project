# 🚀 CrewInsight - Business Analyst Agent

**CrewInsight** is an AI-powered agentic system that collects, analyzes, and summarizes market trends to support strategic business decision-making. Built using **FastAPI**, **OpenAI GPT-4**, and a modular agent architecture, it provides intelligent insights for startups, entrepreneurs, and analysts.

---

## 🧠 Features

- 🔍 Collects market data from configurable sources
- 📊 Analyzes trends using advanced NLP (GPT-4)
- ✍️ Summarizes insights in business-friendly language
- 🧩 Modular agent design (Collector, Analyzer, Summarizer)
- 🔐 API key authentication
- 🧪 Interactive API testing with Swagger UI

---

## 🏗️ Architecture Overview

[Client / Swagger UI / Postman]
↓
[FastAPI]
↓
[Agent Orchestrator (CrewAI-style)]
↓
┌──────────────┬──────────────┬────────────────────┐
│ Data Agent │ Analysis │ Summarization Agent│
│ (collector) │ Agent (GPT-4)│ (OpenAI GPT-4) │
└──────────────┴──────────────┴────────────────────┘


---

## 🛠️ Tech Stack

| Component       | Technology     |
|----------------|----------------|
| Backend         | Python 3.10+   |
| API Framework   | FastAPI        |
| Agents/AI       | OpenAI (GPT-4) |
| Agent Model     | CrewAI-style   |
| Auth            | API Key Header |
| Docs & Testing  | Swagger UI     |

---

## 📦 Project Structure

crewinsight/
├── app/
│ ├── main.py
│ ├── models.py
│ ├── orchestrator.py
│ └── agents/
│ ├── collector.py
│ ├── analyzer.py
│ └── summarizer.py
├── .env
├── requirements.txt
└── README.md


---

## 🚀 Getting Started

### 1. Clone the Repo

```bash

git clone https://github.com/yourusername/crewinsight.git
cd crewinsight


conda create -n openai python==3.10.13
conda activate openai     
pip install -r requirements.txt

```


## OPENAI_API_KEY= your-openai-api-key


## 🧪 Running the API Server

uvicorn app.main:app --reload --port 8000

Visit: http://127.0.0.1:8000/docs for Swagger UI



## app/ folder with:

main.py (FastAPI app)

models.py (Pydantic models)

orchestrator.py (pipeline coordinator)

agents/:

collector.py (mock market data)

analyzer.py (OpenAI-powered trend analyzer)

summarizer.py (OpenAI-powered summarizer)

.env (dummy key — replace with real OpenAI key)

requirements.txt (to install all dependencies)


