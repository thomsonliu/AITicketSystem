import requests
import json


def classify_ticket(ticket_text):

    prompt = f"""
Return ONLY JSON.

Ticket:
{ticket_text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3:8b",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    try:
        return json.loads(result)
    except:
        return {
            "category":"Unknown",
            "priority":"Low",
            "team":"Help Desk"
        }