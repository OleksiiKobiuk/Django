import os

from celery import Celery
from celery.schedules import crontab # можна задати періодичніть запуску завдання

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config_project.settings')

app = Celery('config_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY') # у файлі celery_conf.py шукатиме конфігурацію,
# що починається лише із CELERY

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam-every-minute': {
        'task':'core.tasks.mail_task.spam_mail',
        'schedule': crontab()  # Якщо в круглих скобках crontab() нічого не вказувати, то періодичність буде 1 хв.
    }
}
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')