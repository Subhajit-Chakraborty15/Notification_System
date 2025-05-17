# fast_notify.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from publisher import publish_notification

app = FastAPI()

class NotificationPayload(BaseModel):
    user_id: int
    type: str  # "email", "sms", "in_app"
    message: str

@app.post("/notifications")
def send_notification(payload: NotificationPayload):
    if payload.type not in ["email", "sms", "in_app"]:
        raise HTTPException(status_code=400, detail="Invalid type")

    publish_notification(payload.dict())
    
    return {"status": "Notification sent to queue"}
