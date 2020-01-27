import sys
from PIL import Image
from io import BytesIO

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile

CATEGORY_NAME_MAX_LENGTH = 200
COURSE_NAME_MAX_LENGTH = 200
PROGRAM_ITEM_TITLE_MAX_LENGTH = 200
LINKS_MAX_LENGTH = 2000
TEACHER_NAMES_MAX_LENGTH = 200
LANGUAGE_MAX_LENGTH = 2
LANGUAGE_CHOICES = (
    ('ru', 'Русский'),
    ('kg', 'Кыргызча')
)
DAYS_OF_WEEK = (
    (1, 'Понидельник'),
    (2, 'Вторник'),
    (3, 'Среда'),
    (4, 'Четверг'),
    (5, 'Пятница'),
    (6, 'Суббота'),
    (7, 'Воскресенье')
)


class Category(models.Model):
    name_kg = models.CharField(max_length=CATEGORY_NAME_MAX_LENGTH, verbose_name='Имя на кыргызском')
    name_ru = models.CharField(max_length=CATEGORY_NAME_MAX_LENGTH, verbose_name='Имя на русском')

    def __str__(self):
        return self.name_ru or self.name_ru

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Teacher(models.Model):
    name = models.CharField(max_length=TEACHER_NAMES_MAX_LENGTH, verbose_name='Имя')
    surname = models.CharField(max_length=TEACHER_NAMES_MAX_LENGTH, verbose_name='Фамилия')
    position = models.CharField(max_length=300, verbose_name='Должность')
    language = models.CharField(
        max_length=LANGUAGE_MAX_LENGTH,
        choices=LANGUAGE_CHOICES,
        verbose_name='Язык преподования'
    )
    about_kg = models.TextField(verbose_name='О препод. на кыргызском', null=True)
    about_ru = models.TextField(verbose_name='О препод. на русском', null=True)
    image = models.ImageField(upload_to='teacher/', verbose_name='Изображение')

    def __str__(self):
        return self.name + ' ' + self.surname

    class Meta:
        ordering = ('-id', )
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподователи'

    def __init__(self, *args, **kwargs):
        super(Teacher, self).__init__(*args, **kwargs)
        self._current_image = self.image

    def clean(self):
        image_format = self.image.name.split('.')[-1].lower()
        if image_format not in settings.ALLOWED_IMAGE_FORMATS:
            raise ValidationError('Пожалуйста загрузите фотографию в формате: jpg, jpeg или png!')

        # if self.image.width != self.image.height:
        #     raise ValidationError('Пожалуйста загрузите фотографию с соотношением 1X1.')

    def save(self, *args, **kwargs):
        if self._state.adding or self.image != self._current_image:
            self.image = self.compress_image(self.image)
        super().save(*args, **kwargs)

    def compress_image(self, image):
        image_size = (960, 960)
        image_temproary = Image.open(image)
        output_io_stream = BytesIO()
        image_format = "JPEG" if image.name.split('.')[-1].lower() == 'jpg' else image.name.split('.')[-1]

        if image.width/image_size[0] > image.height/image_size[1]:
            first_height = image.height
            first_width = int(image.width * first_height / image_size[1])
        else:
            first_width = image.width
            first_height = int(image.width * image_size[1] / image_size[0])

        formatted_image = image_temproary.transform(
            (first_width, first_height),
            Image.EXTENT, data=[0, 0, first_width, first_height]
        )
        image_temproary_resized = formatted_image.resize(image_size, Image.ANTIALIAS)
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


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподователь')
    language = models.CharField(
        max_length=LANGUAGE_MAX_LENGTH,
        choices=LANGUAGE_CHOICES,
        verbose_name='Язык проведения'
    )
    name = models.CharField(max_length=COURSE_NAME_MAX_LENGTH, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='course/', verbose_name='Изображение')
    isOnline = models.BooleanField(default=False, verbose_name='Этот курс онлайн?')
    registration_link = models.CharField(
        max_length=LINKS_MAX_LENGTH,
        verbose_name='Ссылка на регистрацию',
        null=True,
        blank=True
    )
    start = models.DateTimeField(verbose_name='Начало трансляции', null=True, blank=True)
    link_to_video = models.CharField(max_length=LINKS_MAX_LENGTH, verbose_name='Ссылка на трансляцию', null=True, blank=True)
    available = models.BooleanField(verbose_name='Опубликовать', default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id', )
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __init__(self, *args, **kwargs):
        super(Course, self).__init__(*args, **kwargs)
        self._current_image = self.image

    def clean(self):
        image_format = self.image.name.split('.')[-1].lower()
        if image_format not in settings.ALLOWED_IMAGE_FORMATS:
            raise ValidationError('Пожалуйста загрузите фотографию в формате: jpg, jpeg или png!')

        # if self.image.width / self.image.height != 16/9:
        #     raise ValidationError('Пожалуйста загрузите фотографию с соотношением 16X9.')

        if self.isOnline:
            if not self.registration_link:
                raise ValidationError('Вы отметили что курс онлайн. Но не заполнили ссылку на регистрацию.')
            if not self.start:
                raise ValidationError('Вы отметили что курс онлайн. Но не заполнили дата и время начало трансляции.')

    def save(self, *args, **kwargs):
        if self._state.adding or self.image != self._current_image:
            self.image = self.compress_image(self.image)
        super().save(*args, **kwargs)

    def compress_image(self, image):
        image_size = (960, 540)
        image_temproary = Image.open(image)
        output_io_stream = BytesIO()
        image_format = "JPEG" if image.name.split('.')[-1].lower() == 'jpg' else image.name.split('.')[-1]

        if image.width/image_size[0] > image.height/image_size[1]:
            first_height = image.height
            first_width = int(image.width * first_height / image_size[1])
        else:
            first_width = image.width
            first_height = int(image.width * image_size[1] / image_size[0])

        formatted_image = image_temproary.transform(
            (first_width, first_height),
            Image.EXTENT, data=[0, 0, first_width, first_height]
        )
        image_temproary_resized = formatted_image.resize(image_size, Image.ANTIALIAS)
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


class ProgramItem(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(verbose_name='Номер')
    title = models.CharField(max_length=PROGRAM_ITEM_TITLE_MAX_LENGTH, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Программы курса'
