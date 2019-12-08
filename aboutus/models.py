from django.db import models
from django.core.exceptions import ValidationError


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Вы можете создать только один О нас.")


class AboutUs(models.Model):
    payload_kg = models.TextField(verbose_name='Контент на кыргызском')
    payload_ru = models.TextField(verbose_name='Контент на русском')

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return 'Текст о нас'

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
