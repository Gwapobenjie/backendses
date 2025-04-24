from models import tasks
from database import database
from schemas import TaskIn

async def get_tasks():
    return await database.fetch_all(tasks.select())

async def create_task(task: TaskIn):
    query = tasks.insert().values(title=task.title, completed=task.completed)
    task_id = await database.execute(query)
    return {**task.dict(), "id": task_id}

async def update_task(task_id: int, task: TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(title=task.title, completed=task.completed)
    await database.execute(query)
    return {**task.dict(), "id": task_id}

async def delete_task(task_id: int):
    await database.execute(tasks.delete().where(tasks.c.id == task_id))
