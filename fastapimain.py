from fastapi import FastAPI
import asyncio
import pika

app = FastAPI()

@app.get("/process-task/")
async def process_task(task_id: int):
    # Симуляция асинхронной обработки задачи
    await asyncio.sleep(2)
    return {"message": f"Task {task_id} processed successfully"}
