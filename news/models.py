from django.db import models
from django.utils.safestring import mark_safe

TITLE_MAX_LENGTH = 200
LOCATION_MAX_LENGTH = 200


class News(models.Model):
    title_kg = models.CharField(max_length=TITLE_MAX_LENGTH, verbose_name='Кыргызча')
    title_ru = models.CharField(max_length=TITLE_MAX_LENGTH, verbose_name='На русском')
    description_kg = models.TextField(verbose_name='Кыргызча')
    description_ru = models.TextField(verbose_name='На русском')
    image = models.ImageField(upload_to='news/', verbose_name='Изображение')
    views = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=False, verbose_name='Опубликовать')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width=500, height=300 >' % self.image)

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title_ru or self.title_kg

    class Meta:
        ordering = ('-id', )
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
