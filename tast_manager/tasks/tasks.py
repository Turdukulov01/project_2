# tasks/tasks.py
from celery import shared_task
from datetime import datetime, timedelta
from .models import Task
import pika

@shared_task
def send_task_reminders():
    now = datetime.now()
    upcoming_tasks = Task.objects.filter(
        due_date__lte=now + timedelta(hours=1), 
        completed=False
    )
    for task in upcoming_tasks:
        print(f"Reminder: Task '{task.title}' is due at {task.due_date}")

def send_to_rabbitmq(task_id):
    """Отправка задачи в RabbitMQ."""
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="tasks", durable=True)

    channel.basic_publish(
        exchange="",
        routing_key="tasks",
        body=str(task_id),
    )
    connection.close()
    
@shared_task
def generate_report(user_id):
    """Генерация отчета для пользователя."""
    # Симуляция длительной работы
    import time
    time.sleep(10)
    return f"Report for user {user_id} generated"