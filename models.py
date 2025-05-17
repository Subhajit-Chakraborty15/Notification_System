
from collections import defaultdict

# Simulating a database
user_notifications = defaultdict(list)

class Notification:
    def __init__(self, user_id, type, message):
        self.user_id = user_id
        self.type = type
        self.message = message
