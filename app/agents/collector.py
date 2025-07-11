import os
import httpx

class MarketDataCollector:
    def fetch_data(self, request):
        api_key = os.getenv("NEWS_API_KEY")
        if not api_key:
            return "News API key not found."

        query = request.market or "technology"
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={query}&"
            f"language=en&"
            f"sortBy=publishedAt&"
            f"pageSize=5&"
            f"apiKey={api_key}"
        )

        try:
            response = httpx.get(url)
            print("NewsAPI raw response:", response.text)  # 🐞 Debug log
            if response.status_code != 200:
                return f"Failed to fetch news: {response.text}"

            articles = response.json().get("articles", [])
            if not articles:
                return "No news articles found."

            content = "\n".join([
                f"{a['title']} - {a['description']}" 
                for a in articles if a['description']
            ])
            return content

        except Exception as e:
            return f"Error fetching news: {str(e)}"
