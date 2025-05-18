import pika
import json

data = {
    "user_id": "2222222",
    "message": "hii",
    "type": "nothing"
}

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='notification_queue', durable=True)

channel.basic_publish(
    exchange='',
    routing_key='notification_queue',
    body=json.dumps(data),
    properties=pika.BasicProperties(delivery_mode=2)
)

connection.close()
print("Sent test message!")
