from sqlalchemy import Table, Column, Integer, String, Boolean
from database import metadata

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("completed", Boolean, default=False)
)
