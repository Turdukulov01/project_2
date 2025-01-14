# kafka/producer.py
from confluent_kafka import Producer

KAFKA_BROKER = "localhost:9092"
TOPIC = "task_logs"

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

producer = Producer({'bootstrap.servers': KAFKA_BROKER})

def log_event(event_message):
    """Отправка события в Kafka."""
    producer.produce(TOPIC, event_message.encode('utf-8'), callback=delivery_report)
    producer.flush()
