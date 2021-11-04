# сервіс для відправки пошти при реєстрації юзера

# метод, щоб витягнути темплейт із register.mail.html і передати його в лист
from django.core.mail import EmailMultiAlternatives
# екземпляр класу, що займається відправкою пошти
from django.template.loader import get_template
from django.contrib.auth import get_user_model

from config_project import settings

UserModel = get_user_model()


class MailService:
    @staticmethod
    def register_mail_sender(username, to):
        template = get_template('register_mail.html')
        html_content = template.render({"username": username})
        msg = EmailMultiAlternatives('Registration email', 'Hello', 'promotion.ias@gmail.com', [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @staticmethod
    def spam_mail_sender():
        to = [user.email for user in UserModel.objects.all()]
        template = get_template('spam.html')
        html_content = template.render()
        msg = EmailMultiAlternatives('SPAM', from_email=settings.EMAIL_HOST_USER, to=to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

