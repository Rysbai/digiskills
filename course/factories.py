import datetime

import factory
from django.db.models.signals import post_save

from course.models import Category, Teacher, Course, ProgramItem, LANGUAGE_CHOICES


@factory.django.mute_signals(post_save)
class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    category = factory.SubFactory('course.factories.CategoryFactory', course=None)
    teacher = factory.SubFactory('course.factories.TeacherFactory', course=None)

    language = LANGUAGE_CHOICES[0][0]
    name = 'Example name'
    description ='Example name'
    image = factory.django.ImageField(image_name='image.png')
    isOnline = True
    registration_link = 'example.com/link'
    start = datetime.datetime.now()
    link_to_video = 'example.com/link'
    available = True

    @staticmethod
    def create_many(category, teacher, language='ru', count=3):
        courses = []
        for i in range(count):
            courses.append(
                CourseFactory(category=category, teacher=teacher, language=language)
            )
        return courses


@factory.django.mute_signals(post_save)
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name_kg = 'Example name in kyrgyz'
    name_ru = 'Example name in russian'

    course = factory.RelatedFactory(CourseFactory, 'category')

    @staticmethod
    def create_many(count=3):
        categories = []
        for i in range(count):
            categories.append(CategoryFactory())
        return categories


@factory.django.mute_signals(post_save)
class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Teacher

    name = 'Example name'
    surname = 'Example surname'
    position = 'Example position'
    language = LANGUAGE_CHOICES[0][0]
    about_kg = 'Example about in kyrgyz'
    about_ru = 'Example about in russian'
    image = factory.django.ImageField(image_name='image.png')

    course = factory.RelatedFactory(CourseFactory, 'teacher')

    @staticmethod
    def create_many(count=3):
        teachers = []
        for i in range(count):
            teachers.append(TeacherFactory())

        return teachers





