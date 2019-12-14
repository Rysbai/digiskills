import os
from celery import Celery
import django
from django.conf import settings
from django.core.mail import send_mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digiskills.settings')
django.setup()
from django.contrib.auth.models import User

app = Celery('digiskills')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


@app.task
def send_comment_to_admin_email(comment):
    admin = User.objects.filter(is_superuser=True)[0]
    subject = 'Комментарий к проекту digiskills от {}'.format(comment['name'])
    text = 'Комментарий от {}\n'.format(comment['name']) + \
           'Номер телефона: {}\n'.format(comment['phone']) + \
           comment['text']

    try:
        send_mail(
            subject,
            text,
            settings.EMAIL_HOST_USER,
            [admin.email],
            fail_silently=False,
        )
    except Exception as exception:
        print('**********************************************************************************************************')
        print(exception)
