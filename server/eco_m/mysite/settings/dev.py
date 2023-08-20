from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&w1($hz0p610iq!6^q7a_6x+_b5!xhf@l@ib%@huatp$t)tre#"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [
    "0.0.0.0",
    "127.0.0.1"
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
