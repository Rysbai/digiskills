from django.conf import settings
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.models import User


def send_comment_to_admin_email(name: str, phone: str, text: str, *args, **kwargs):
    admins = User.objects.filter(~Q(email=''), is_superuser=True)
    subject = 'Комментарий к проекту digiskills от {}'.format(name)
    text = 'Комментарий от {}\n'.format(name) + \
           'Номер телефона: {}\n'.format(phone) + \
           text

    for admin in admins:
        try:
            send_mail(
                subject,
                text,
                settings.EMAIL_HOST_USER,
                [admin.email],
                fail_silently=False,
            )
        except Exception as exception:
            pass
