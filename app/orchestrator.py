import uuid
from app.agents.collector import MarketDataCollector
from app.agents.analyzer import TrendAnalyzer
from app.agents.summarizer import SummaryGenerator

class AgentOrchestrator:
    def run_pipeline(self, request):
        data = MarketDataCollector().fetch_data(request)
        trends = TrendAnalyzer().analyze(data)
        summary = SummaryGenerator().summarize(trends)
        return {
            "request_id": str(uuid.uuid4()),
            "summary": summary,
            "trends": trends
        }
