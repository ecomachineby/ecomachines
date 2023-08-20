import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

JWT_SECRET = os.getenv("JWT_SECRET")
