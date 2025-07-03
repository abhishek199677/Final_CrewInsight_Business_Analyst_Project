class MarketDataCollector:
    def fetch_data(self, request):
        return f"Sample market data for {request.market} in {request.region} during {request.timeframe}"
