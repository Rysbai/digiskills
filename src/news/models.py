import sys
from PIL import Image
from io import BytesIO

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.conf import settings


TITLE_MAX_LENGTH = 200
LOCATION_MAX_LENGTH = 200


class News(models.Model):
    title_kg = models.CharField(max_length=TITLE_MAX_LENGTH, verbose_name='Кыргызча', blank=True)
    title_ru = models.CharField(max_length=TITLE_MAX_LENGTH, verbose_name='На русском', blank=True)
    description_kg = models.TextField(verbose_name='Кыргызча', blank=True)
    description_ru = models.TextField(verbose_name='На русском', blank=True)
    image = models.ImageField(upload_to='news/', verbose_name='Изображение')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.title_ru or self.title_kg

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __init__(self, *args, **kwargs):
        super(News, self).__init__(*args, **kwargs)
        self._current_image = self.image

    def save(self, *args, **kwargs):
        if self._state.adding or self.image != self._current_image:
            self.image = self.compress_image(self.image)
        super().save(*args, **kwargs)

    def compress_image(self, image):
        image_size = (960, 540)
        image_temporary = Image.open(image)
        output_io_stream = BytesIO()
        image_format = "JPEG" if image.name.split('.')[-1].lower() == 'jpg' else image.name.split('.')[-1]

        x0, y0 = 0, 0
        if image.width/image_size[0] > image.height/image_size[1]:
            y1 = image.height
            x1 = int(image_size[0] * y1 / image_size[1])
        else:
            x1 = image.width
            y1 = int(image_size[1] * x1 / image_size[0])

        formatted_image = image_temporary.transform(
            (x1, y1),
            Image.EXTENT, data=[x0, y0, x1, y1]
        )
        image_temporary_resized = formatted_image.resize(image_size, Image.ANTIALIAS)
        image_temporary_resized.save(output_io_stream, format=image_format)
        output_io_stream.seek(0)
        uploaded_image = InMemoryUploadedFile(
            output_io_stream,
            'ImageField',
            image.name,
            'image/{}'.format(image_format),
            sys.getsizeof(output_io_stream),
            None
        )
        return uploaded_image

    def clean(self):
        image_format = self.image.name.split('.')[-1].lower()
        if image_format not in settings.ALLOWED_IMAGE_FORMATS:
            raise ValidationError('Пожалуйста загрузите фотографию в формате: jpg, jpeg или png!')

        if not self.title_kg and not self.title_ru:
            raise ValidationError('Пожалуйста заполните поле ЗАГОЛОВОК НОВОСТИ хотя бы на русском или на кыргызском.')
        if not self.description_kg and not self.description_ru:
            raise ValidationError('Пожалуйста заполните поле ОПИСАНИЕ НОВОСТИ хотя бы на русском или на кыргызском.')
