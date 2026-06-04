from sqlalchemy import *

metadata = MetaData()

tickets = Table(
    "tickets",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("description", String),
    Column("category", String),
    Column("priority", String),
    Column("team", String)
)