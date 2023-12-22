import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerylearn.settings')
app = Celery('celerylearn')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()