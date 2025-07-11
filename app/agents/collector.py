import os
import httpx
from dotenv import load_dotenv

load_dotenv()

class MarketDataCollector:
    def fetch_data(self, request):
        api_key = os.getenv("NEWS_API_KEY")
        query = request.market
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={query}&"
            f"language=en&"
            f"sortBy=publishedAt&"
            f"pageSize=5&"
            f"apiKey={api_key}"
        )

        response = httpx.get(url)
        if response.status_code != 200:
            return f"Failed to fetch news: {response.text}"

        articles = response.json().get("articles", [])
        if not articles:
            return "No news articles found."

        # Combine all titles + descriptions as a string
        content = "\n".join([f"{a['title']} - {a['description']}" for a in articles if a['description']])
        return content
