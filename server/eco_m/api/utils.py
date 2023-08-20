import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import jwt
from rest_framework.request import Request

from config import EMAIL, JWT_SECRET, EMAIL_HOST, EMAIL_PORT, PASSWORD
from mysite.settings import base


def create_jwt(user):
    payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
        "iat": datetime.datetime.utcnow(),
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256").decode("utf-8")
    return token


def decode_jwt(token):
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256", ])


def get_url_file(field, request: Request):
    video_url = None
    if field:
        video_path = os.path.join(
            base.MEDIA_ROOT,
            field.url,
        )
        video_url = request.build_absolute_uri(video_path)
    return video_url


def email_common(subject, body):
    try:
        message = MIMEMultipart()
        message["From"] = EMAIL
        message["To"] = EMAIL
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(message)

        return "Success"

    except smtplib.SMTPServerDisconnected as e:
        return f"SMTP Server Disconnected: {e}"

    except Exception as e:
        return f"Error sending email: {e}"


class MessageHandler:
    def __init__(self, validated_data):
        self.message = None

        self.profile = validated_data.get("profile", None)
        self.value = validated_data.get("value", None)
        self.text = validated_data.get("text", None)
        self.email = validated_data.get("email", None)
        self.value = validated_data.get("value", None)
        self.phone = validated_data.get("phone", None)
        self.service = validated_data.get("service", None)
        self.organization = validated_data.get("organization", None)

    def get_body(self):
        body = ""
        if self.profile:
            body += f"User: {self.profile}\n"

        if self.value:
            body += f"Value: {self.value}\n"
        if self.text:
            body += f"Text: {self.text}\n"
        if self.organization:
            body += f"Organization: {self.organization}\n"
        if self.email:
            body += f"Email: {self.email}\n"
        if self.phone:
            body += f"Phone: {self.phone}\n"
        if self.service:
            body += f"Service: {self.service}\n"

        self.message = body

    def main(self):
        self.get_body()
        return self.message
