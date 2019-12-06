from django.db import models
from django.utils.safestring import mark_safe

TEACHER_NAMES_MAX_LENGTH = 200
LANGUAGE_MAX_LENGTH = 2
LANGUAGE_CHOICES = (
    ('ru', 'Русский'),
    ('kg', 'Кыргызча')
)


class Teacher(models.Model):
    name = models.CharField(max_length=TEACHER_NAMES_MAX_LENGTH, verbose_name='Имя')
    surname = models.CharField(max_length=TEACHER_NAMES_MAX_LENGTH, verbose_name='Фамилия')
    language = models.CharField(max_length=LANGUAGE_MAX_LENGTH, choices=LANGUAGE_CHOICES, verbose_name='Язык преподования')
    about_kg = models.TextField(verbose_name='О препод. на кыргызском')
    about_ru = models.TextField(verbose_name='О препод. на русском')
    image = models.ImageField(verbose_name='Изображение')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width=400, height=300 >' % self.image)

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name + self.surname

    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподователи'
