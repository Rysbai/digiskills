import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
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
        return mark_safe('<img src="/media/{}" width="50%", height="50%" >'.format(self.image))

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title_ru or self.title_kg

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __init__(self, *args, **kwargs):
        super(News, self).__init__(*args, **kwargs)
        self._past_image = self.image

    def save(self, *args, **kwargs):
        is_create = False
        if self._state.adding:
            is_create = True
        if is_create or self._past_image != self.image:
            self.image = self.compress_image(self.image)
            self._past_image = self.image

        super().save(*args, **kwargs)

    def compress_image(self, image):
        image_size = (960, 540)
        image_temproary = Image.open(image)
        output_io_stream = BytesIO()
        image_format = "JPEG" if image.name.split('.')[-1].lower() == 'jpg' else image.name.split('.')[-1]

        image_temproary_resized = image_temproary.resize(image_size, Image.ANTIALIAS)
        image_temproary_resized.save(output_io_stream, format=image_format)
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
