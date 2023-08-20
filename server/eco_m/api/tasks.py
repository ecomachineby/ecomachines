from smtplib import SMTPServerDisconnected

from django.core.mail import send_mail
from config import (
    EMAIL,
)
from mysite.celery import app


@app.task
def email_task(subject: str, message: str):
    try:
        send_mail(
            subject=subject,
            from_email=EMAIL,
            recipient_list=[EMAIL, ],
            message=message,
        )

        return "Good"

    except SMTPServerDisconnected as e:
        print(f"SMTP Server Disconnected: {e}")
        raise

    except Exception as e:
        print(f"Error sending email: {e}")
        raise

