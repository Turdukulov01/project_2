from fastapi import FastAPI
from .tasks import process_task

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI module is running"}

@app.post("/process-task/")
async def process_task_endpoint(task_id: int):
    """Эндпоинт для обработки задач."""
    result = await process_task(task_id)
    return {"message": f"Task {task_id} processed", "result": result}
