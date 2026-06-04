from fastapi import FastAPI

app = FastAPI()

tickets = []

@app.post("/ticket")
def create_ticket(ticket: dict):
    tickets.append(ticket)
    return {"message": "Ticket created"}