
import pika
import json

def publish_notification(notification):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    
    channel.queue_declare(queue='notification_queue', durable=True)
    
    channel.basic_publish(
        exchange='',
        routing_key='notification_queue',
        body=json.dumps(notification),
        properties=pika.BasicProperties(delivery_mode=2)  # make message persistent
    )
    connection.close()
