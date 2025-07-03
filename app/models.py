from pydantic import BaseModel
from typing import List

class MarketRequest(BaseModel):
    market: str
    region: str
    timeframe: str

class SummaryResponse(BaseModel):
    request_id: str
    summary: str
    trends: List[str]
