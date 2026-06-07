import requests
import json

def classify_ticket(ticket_text):

    prompt = f"""
You are an IT Service Desk AI.

Classify the ticket.

Categories:
- Network
- Hardware
- Software
- Email
- Security

Priorities:
- Low
- Medium
- High
- Critical

Return ONLY JSON.

Example:

{{
    "category":"Network",
    "priority":"High",
    "team":"Network Team"
}}

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
    except Exception:
        return {
            "category": "Unknown",
            "priority": "Low",
            "team": "Help Desk"
        }