import json

from django.test import TestCase

from course.factories import CourseFactory, CategoryFactory, TeacherFactory
from course.models import Course
from course.serializers import CategorySerializer, CourseSerializer, TeacherSerializer
from utils.get_absolute_url import get_media_absolute_url


class CategoryAPITest(TestCase):
    def test_should_return_all_categories_in_kyrgyz_by_default(self):
        categories = CategoryFactory.create_many()
        path = '/api/course/categories/'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            CategorySerializer(categories, many=True, lang='kg').data
        )

    def test_should_return_all_categories_in_russian_if_lang_is_ru(self):
        categories = CategoryFactory.create_many()
        path = '/api/course/categories/?lang=ru'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            CategorySerializer(categories, many=True, lang='ru').data
        )

    def test_should_return_category_by_id_in_kyrgyz_by_default(self):
        category = CategoryFactory()
        path = '/api/course/categories/{}/'.format(category.id)

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            CategorySerializer(category, lang='kg').data
        )

    def test_should_return_category_by_id_in_russian_if_lang_is_ru(self):
        category = CategoryFactory()
        path = '/api/course/categories/{}/?lang=ru'.format(category.id)

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            CategorySerializer(category, lang='ru').data
        )


class TeacherAPITest(TestCase):
    def test_should_return_all_teachers_in_kyrgyz_content_by_default(self):
        teachers = TeacherFactory.create_many()
        path = '/api/course/teachers/'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            TeacherSerializer(teachers, many=True, lang='kg').data
        )

    def test_should_return_all_teachers_in_russian_content_if_lang_is_ru(self):
        teachers = TeacherFactory.create_many()
        path = '/api/course/teachers/?lang=ru'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            TeacherSerializer(teachers, many=True, lang='ru').data
        )

    def test_should_return_teacher_by_id_in_kyrgyz_content_by_default(self):
        teacher = TeacherFactory()
        path = '/api/course/teachers/{}/'.format(teacher.id)

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            TeacherSerializer(teacher, lang='kg').data
        )

    def test_should_return_teacher_by_id_in_russian_content_if_lang_is_ru(self):
        teacher = TeacherFactory()
        path = '/api/course/teachers/{}/?lang=ru'.format(teacher.id)

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            TeacherSerializer(teacher, lang='ru').data
        )
