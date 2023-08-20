import os

from celery import Celery

from mysite.settings import base

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'mysite.settings.base'
)

app = Celery("mysite")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
