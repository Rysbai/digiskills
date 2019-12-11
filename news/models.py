from django.db import models
from django.utils.timezone import datetime
from django.utils.safestring import mark_safe

TITLE_MAX_LENGTH = 200
LOCATION_MAX_LENGTH = 200


class News(models.Model):
    title_kg = models.CharField(max_length=TITLE_MAX_LENGTH, verbose_name='Кыргызча', null=True)
    title_ru = models.CharField(max_length=TITLE_MAX_LENGTH, verbose_name='На русском', null=True)
    description_kg = models.TextField(verbose_name='Кыргызча', blank=True)
    description_ru = models.TextField(verbose_name='На русском', blank=True)
    image = models.ImageField(upload_to='news/', verbose_name='Изображение')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    pub_date = models.DateTimeField(default=datetime.now(), verbose_name='Дата публикации')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width=600, height=400 >' % self.image)

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title_ru or self.title_kg

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
