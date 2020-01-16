from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=200, verbose_name='Номер телефона')
    text = models.TextField(verbose_name='Текст')
    available = models.BooleanField(default=False, verbose_name='Опубликовать')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name
