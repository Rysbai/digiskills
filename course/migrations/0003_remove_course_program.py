# Generated by Django 2.2.7 on 2019-12-04 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_programitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='program',
        ),
    ]
