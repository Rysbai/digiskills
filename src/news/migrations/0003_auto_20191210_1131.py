# Generated by Django 2.2.7 on 2019-12-10 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20191210_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
    ]
