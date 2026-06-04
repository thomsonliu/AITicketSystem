import requests
import json

def classify_ticket(ticket_text):

    prompt = f"""
    Classify this IT ticket.

    Categories:
    Network
    Hardware
    Software
    Email
    Security

    Return JSON only.

    Ticket:
    {ticket_text}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    return result