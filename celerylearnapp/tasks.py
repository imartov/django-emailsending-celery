from .models import Contact
from django.core.mail import send_mail
from celerylearn.celery import app

from .service import send


@app.task
def send_spam_email(user_mail):
    send(user_mail)

# @app.task
# def send_beat_email():
#     for contact in Contact.objects.all():
#         send_mail(
#             'Вы подписались на рассылку',
#             'Мы будем присылать Вам много спама',
#             'pythontest285@gmail.com',
#             [contact.email],
#             fail_silently=False
#         )
