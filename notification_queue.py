
from utils import notify_user
from models import user_notifications, Notification
import time

retry_limit = 3

def process_notification(type, user_id, message):
    success = False
    for attempt in range(retry_limit):
        print(f"Attempt {attempt+1} for User {user_id}")
        success = notify_user(type, user_id, message)
        if success:
            break
        time.sleep(1)  # Retry delay
    return success

def enqueue_notification(type, user_id, message):
    success = process_notification(type, user_id, message)
    if success:
        notif = Notification(user_id, type, message)
        user_notifications[user_id].append(notif)
    else:
        print(f"[Error] Failed to deliver to User {user_id} after retries.")
