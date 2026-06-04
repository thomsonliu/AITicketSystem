# test.py

from app.ai.classifier import classify_ticket

ticket = """
Cannot connect to company VPN after Windows update
"""

result = classify_ticket(ticket)

print(result)