
import pika
import json
import time
from utils import notify_user
from models import user_notifications, Notification

def callback(ch, method, properties, body):
    data = json.loads(body)
    user_id = data['user_id']
    notif_type = data['type']
    message = data['message']

    for attempt in range(3):
        print(f"Processing notification for User {user_id} (Attempt {attempt+1})")
        success = notify_user(notif_type, user_id, message)
        if success:
            notif = Notification(user_id, notif_type, message)
            user_notifications[user_id].append(notif)
            ch.basic_ack(delivery_tag=method.delivery_tag)
            print("Notification sent and acknowledged.")
            return
        time.sleep(1)

    print(f"Failed to send notification to User {user_id}")
    # (You can choose to dead-letter this if needed)

def start_worker():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue='notification_queue', durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='notification_queue', on_message_callback=callback)

    print("Worker started. Waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    start_worker()
