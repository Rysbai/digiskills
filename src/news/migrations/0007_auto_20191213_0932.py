# Generated by Django 2.2.7 on 2019-12-13 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20191212_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 13, 9, 31, 25, 133221), verbose_name='Дата публикации'),
        ),
    ]
