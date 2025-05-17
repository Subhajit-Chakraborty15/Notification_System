
from flask import Flask, jsonify
from models import user_notifications

app = Flask(__name__)

@app.route("/users/<int:user_id>/notifications", methods=["GET"])
def get_user_notifications(user_id):
    notifs = user_notifications.get(user_id, [])
    result = [{"type": n.type, "message": n.message} for n in notifs]
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000)
