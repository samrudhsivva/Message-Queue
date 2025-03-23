# Sends 10,000 messages to RabbitMQ

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(1, 10001):
    message = f"Message {i}"
    channel.basic_publish(exchange='', routing_key='hello', body=message)

print("✅ Sent 10,000 messages.")
connection.close()
