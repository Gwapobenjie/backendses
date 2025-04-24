from fastapi import FastAPI
from env.database import database, engine, metadata
from schemas import Task, TaskIn
from crud import get_tasks, create_task, update_task, delete_task

app = FastAPI()
metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/tasks/", response_model=list[Task])
async def read_tasks():
    return await get_tasks()

@app.post("/tasks/", response_model=Task)
async def add_task(task: TaskIn):
    return await create_task(task)

@app.put("/tasks/{task_id}/", response_model=Task)
async def edit_task(task_id: int, task: TaskIn):
    return await update_task(task_id, task)

@app.delete("/tasks/{task_id}/")
async def remove_task(task_id: int):
    await delete_task(task_id)
    return {"message": "Deleted"}
