import aio_pika
import asyncio
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

RABBITMQ_URL = "amqp://guest:guest@localhost/"


async def process_task(task_id: int):
    """Асинхронная обработка задачи."""
    # Симуляция длительной обработки задачи
    await asyncio.sleep(5)  # Замените реальной логикой обработки
    return {"task_id": task_id, "status": "completed"}


async def process_task_from_queue():
    """Обработка задач из очереди RabbitMQ."""
    try:
        connection = await aio_pika.connect_robust(RABBITMQ_URL)
        async with connection:
            channel = await connection.channel()
            queue = await channel.declare_queue("tasks", durable=True)

            async for message in queue:
                async with message.process():
                    task_id = int(message.body.decode())
                    logger.info(f"Received task {task_id}")
                    result = await process_task(task_id)
                    logger.info(f"Task {task_id} processed: {result}")
    except Exception as e:
        logger.error(f"Error processing tasks: {e}")
