
def send_email(user_id, message):
    print(f"[Email] Sent to User {user_id}: {message}")
    return True

def send_sms(user_id, message):
    print(f"[SMS] Sent to User {user_id}: {message}")
    return True

def send_in_app(user_id, message):
    print(f"[In-App] Stored for User {user_id}: {message}")
    return True

def notify_user(type, user_id, message):
    if type == 'email':
        return send_email(user_id, message)
    elif type == 'sms':
        return send_sms(user_id, message)
    elif type == 'in_app':
        return send_in_app(user_id, message)
    return False
