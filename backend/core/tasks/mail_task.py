from config_project.celery import app
from core.services.mail_service import MailService

@app.task
def mail_send_task(username, to):
    MailService.register_mail_sender(username, to)

@app.task
def spam_mail():
    MailService.spam_mail_sender()
