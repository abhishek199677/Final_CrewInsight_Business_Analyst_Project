from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SummaryGenerator:
    def summarize(self, trends):
        prompt = "Summarize the following market trends for business stakeholders:\n" + "\n".join(trends)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a business report summarizer."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
