from django.core.mail import send_mail


def send(user_mail) -> None:
    send_mail(
        'Вы подписались на рассылку',
        'Мы будем присылать Вам много спама',
        'pythontest285@gmail.com',
        [user_mail],
        fail_silently=False
    )