# Generated by Django 2.2.7 on 2019-12-12 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20191210_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description_kg',
            field=models.TextField(blank=True, verbose_name='Кыргызча'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description_ru',
            field=models.TextField(blank=True, verbose_name='На русском'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 12, 21, 26, 37, 880627), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_kg',
            field=models.CharField(max_length=200, null=True, verbose_name='Кыргызча'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='На русском'),
        ),
    ]
