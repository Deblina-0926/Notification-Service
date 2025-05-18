import pika
import json

def publish_notification(data):
    try:
        print("Connecting to RabbitMQ from publisher...")
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        print("Connected to RabbitMQ!")
        channel = connection.channel()
        channel.queue_declare(queue='notification_queue', durable=True)
        channel.basic_publish(
            exchange='',
            routing_key='notification_queue',
            body=json.dumps(data),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        connection.close()
        print("Notification published!")
    except Exception as e:
        print(f"Error publishing notification: {e}")
