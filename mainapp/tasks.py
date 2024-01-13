import time

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django_rq import job


@job('high')
def send_email_to_user(email, topic, message):
    print('Начали готовить письмо для пользователя...')
    time.sleep(5)
    # готовим и отправляем письмо на почту со ссылкой для смены пароля

    context = {
        'email': email,
        'topic': topic,
        'message': message,
    }
    email_html_message = render_to_string('mainapp/mail_templates/send_mail_to_user.html', context=context)

    # отправляем письмо
    send_mail(
        subject=_('Вас приветствует обучающая платформа!'),
        message=_(topic),
        from_email="edu_platform@gmail.com",
        html_message=email_html_message,
        recipient_list=[email, ]
    )

    print('Отправили письмо пользователю!')


@job('high')
def send_email_to_admin(email, topic, message):
    print('Начали готовить письмо для админа...')
    time.sleep(5)

    # отправляем письмо админу
    send_mail(
        subject=_('У нас новое обращение'),
        message=_(f'тема:{topic}. \n Сообщение:{message}. От кого: {email}'),
        from_email=email,
        recipient_list=['admin@edu.ru', ]
    )

    print('Отправили письмо админу!')
