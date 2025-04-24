from pydantic import BaseModel

class TaskIn(BaseModel):
    title: str
    completed: bool = False

class Task(TaskIn):
    id: int
