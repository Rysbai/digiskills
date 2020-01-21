from django.db import models

CONTACT_TYPES = [('phone', "Телефон"), ('facebook', "Facebook"), ('email', "Email"), ('instagram', "Instagram")]
VALUE_MAX_LENGTH = 200


class Contact(models.Model):
    type = models.CharField(choices=CONTACT_TYPES, max_length=100, verbose_name='Тип контакта')
    value = models.CharField(max_length=VALUE_MAX_LENGTH, verbose_name='Значение')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
