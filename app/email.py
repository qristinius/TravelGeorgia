from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from threading import Thread

from app.extensions import mail
from app.config import Config, Constant


def send_email(subject, text, recipients):
    message = Message(subject=subject, html=text, recipients=[recipients], sender="TrevelGeorgia")
    thread = Thread(target=mail.send(message))
    thread.start()


def create_key(payload):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    key = serializer.dumps(payload, salt=Constant.SERIALIZER_SALT)
    return key


def confirm_key(key):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    try:
        payload = serializer.loads(key, salt=Constant.SERIALIZER_SALT, max_age=600)
        return payload
    except:
        return False




