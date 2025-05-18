import pika
import json

def callback(ch, method, properties, body):
    print("[x] Received %r" % body)
    data = json.loads(body)
    print(f"[✔] Processing notification for user {data['user_id']} with message: {data['message']} and type: {data['type']}")

print("Connecting to RabbitMQ...")
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
print("Connected!")

channel = connection.channel()
channel.queue_declare(queue='notification_queue', durable=True)

channel.basic_consume(queue='notification_queue', on_message_callback=callback, auto_ack=True)

print('[*] Waiting for messages...')
channel.start_consuming()
