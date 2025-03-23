# Receives messages and verifies no loss

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message_count = 0
expected_messages = 10000

def callback(ch, method, properties, body):
    global message_count
    message_count += 1

    if message_count % 1000 == 0:
        print(f"✅ Received {message_count} messages...")

    if message_count >= expected_messages:
        print(f"\n🎉 All {message_count} messages received successfully!")
        connection.close()

channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

print('🔄 Waiting for messages...')
channel.start_consuming()
