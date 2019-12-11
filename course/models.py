import sys
from PIL import Image
from io import BytesIO
from django.db import models
from django.utils.safestring import mark_safe
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

    def image_tag(self):
        return mark_safe('<img src="/media/{}" width="50%", height="50%" >'.format(self.image))

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name + ' ' + self.surname

    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподователи'

    def __init__(self, *args, **kwargs):
        super(Teacher, self).__init__(*args, **kwargs)
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
        image_size = (1020, 1020)
        image_temproary = Image.open(image)
        output_io_stream = BytesIO()
        image_format = "JPEG" if image.name.split('.')[-1] == 'jpg' else image.name.split('.')[-1]

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


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподователь')
    language = models.CharField(
        max_length=LANGUAGE_MAX_LENGTH,
        choices=LANGUAGE_CHOICES,
        verbose_name='Язык проведения'
    )
    name_kg = models.CharField(max_length=COURSE_NAME_MAX_LENGTH, verbose_name='На кыргызском', null=True)
    name_ru = models.CharField(max_length=COURSE_NAME_MAX_LENGTH, verbose_name='На русском', null=True)
    description_kg = models.TextField(verbose_name='На кыргызском', blank=True)
    description_ru = models.TextField(verbose_name='На русском', blank=True)
    image = models.ImageField(upload_to='course/', verbose_name='Изображение')
    registration_link = models.CharField(max_length=CATEGORY_NAME_MAX_LENGTH, verbose_name='Ссылка на регистрацию')
    start = models.DateField(verbose_name='Начало')
    end = models.DateField(verbose_name='Конец')
    available = models.BooleanField(verbose_name='Опубликовать', default=False)

    def image_tag(self):
        return mark_safe('<img src="/media/{}" width="50%", height="50%" >'.format(self.image))

    image_tag.short_description = 'Превю изображения(можно видеть после сохранения)'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name_ru or self.name_kg

    class Meta:
        ordering = ('-id', )
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __init__(self, *args, **kwargs):
        super(Course, self).__init__(*args, **kwargs)
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
        image_size = (1200, 900)
        image_temproary = Image.open(image)
        output_io_stream = BytesIO()
        image_format = "JPEG" if image.name.split('.')[-1] == 'jpg' else image.name.split('.')[-1]

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


class ScheduleItem(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS_OF_WEEK, verbose_name='День недели')
    time = models.TimeField(verbose_name='Время')

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Расписание курса'


class ProgramItem(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=PROGRAM_ITEM_TITLE_MAX_LENGTH, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Программы курса'


class Material(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description_kg = models.CharField(max_length=500, verbose_name='Описание(Kg)', null=True)
    description_ru = models.CharField(max_length=500, verbose_name='Описание(Ru)', null=True)
    link = models.CharField(max_length=CATEGORY_NAME_MAX_LENGTH, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы круса'


class VideoLesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description_kg = models.CharField(max_length=500, verbose_name='Описание(Kg)', null=True)
    description_ru = models.CharField(max_length=500, verbose_name='Описание(Ru)', null=True)
    link = models.CharField(max_length=CATEGORY_NAME_MAX_LENGTH, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Видео курса'
        verbose_name_plural = 'Видео курса'
