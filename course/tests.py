from django.test import TestCase
from django.urls import reverse

from course.factories import CourseFactory, CategoryFactory, TeacherFactory
from course.models import Course
from course.serializers import CategorySerializer, CourseSerializer, TeacherSerializer
from utils.get_absolute_url import get_media_absolute_url


class CategoryAPITest(TestCase):
    def test_should_return_all_categories_in_kyrgyz_by_default(self):
        categories = CategoryFactory.create_many()
        path = reverse('course:category_list')

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            CategorySerializer(categories, many=True, lang='kg').data
        )

    def test_should_return_all_categories_in_russian_if_lang_is_ru(self):
        categories = CategoryFactory.create_many()
        path = reverse('course:category_list') + '?lang=ru'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            CategorySerializer(categories, many=True, lang='ru').data
        )

    def test_should_return_category_by_id_in_kyrgyz_by_default(self):
        category = CategoryFactory()
        path = reverse('course:category_detail', args=[category.id])

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            CategorySerializer(category, lang='kg').data
        )

    def test_should_return_category_by_id_in_russian_if_lang_is_ru(self):
        category = CategoryFactory()
        path = reverse('course:category_detail', args=[category.id]) + '?lang=ru'

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
        path = reverse('course:teacher_list')

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            TeacherSerializer(teachers, many=True, lang='kg').data
        )

    def test_should_return_all_teachers_in_russian_content_if_lang_is_ru(self):
        teachers = TeacherFactory.create_many()
        path = reverse('course:teacher_list') + '?lang=ru'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            TeacherSerializer(teachers, many=True, lang='ru').data
        )

    def test_should_return_teacher_by_id_in_kyrgyz_content_by_default(self):
        teacher = TeacherFactory()
        path = reverse('course:teacher_detail', args=[teacher.id])

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            TeacherSerializer(teacher, lang='kg').data
        )

    def test_should_return_teacher_by_id_in_russian_content_if_lang_is_ru(self):
        teacher = TeacherFactory()
        path = reverse('course:teacher_detail', args=[teacher.id]) + '?lang=ru'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data,
            TeacherSerializer(teacher, lang='ru').data
        )


class CourseAPITest(TestCase):
    def assert_equal_course(self, body: dict, course_orm: Course):
        self.assertEqual(body['teacher_id'], course_orm.teacher_id)
        self.assertEqual(body['category_id'], course_orm.category_id)
        self.assertEqual(body['language'], course_orm.language)
        self.assertEqual(body['description'], course_orm.description)
        self.assertEqual(body['image'], get_media_absolute_url(course_orm.image.url))
        self.assertEqual(body['isOnline'], course_orm.isOnline)
        self.assertEqual(body['registration_link'], course_orm.registration_link)
        # self.assertEqual(body['start'], course_orm.start)
        self.assertEqual(body['link_to_video'], course_orm.link_to_video)
        self.assertEqual(body['available'], course_orm.available)

    def test_should_return_all_courses_in_both_of_languages(self):
        category = CategoryFactory(course=None)
        teacher = TeacherFactory(course=None)
        courses = CourseFactory.create_many(category, teacher)
        courses.reverse()
        path = reverse('course:course_list')

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['total'], len(courses))
        for i in range(len(courses)-1):
            self.assert_equal_course(data['data'][i], courses[i])

    def test_should_return_all_courses_in_specific_lang_if_lang_query_param_provided(self):
        category = CategoryFactory(course=None)
        teacher = TeacherFactory(course=None)
        courses = CourseFactory.create_many(category, teacher)
        courses.reverse()
        path = reverse('course:course_list')

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['total'], len(courses))
        for i in range(len(courses)-1):
            self.assert_equal_course(data['data'][i], courses[i])

    def test_should_return_filtered_courses_by_category_id(self):
        category = CategoryFactory(course=None)
        teacher = TeacherFactory(course=None)
        courses = CourseFactory.create_many(category, teacher)
        courses.reverse()
        courses_with_another_category = CourseFactory.create_many(CategoryFactory(course=None), teacher)
        path = reverse('course:course_list') + '?category_id={}'.format(category.id)

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['total'], len(courses))
        for i in range(len(courses)-1):
            self.assert_equal_course(data['data'][i], courses[i])

    def test_should_return_filtered_courses_by_teacher_id(self):
        category = CategoryFactory(course=None)
        teacher = TeacherFactory(course=None)
        courses = CourseFactory.create_many(category, teacher)
        courses.reverse()
        courses_with_another_teacher = CourseFactory.create_many(category, TeacherFactory(course=None))
        path = reverse('course:course_list') + '?teacher_id={}'.format(teacher.id)

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['total'], len(courses))
        for i in range(len(courses)-1):
            self.assert_equal_course(data['data'][i], courses[i])

    def test_should_return_filtered_courses_by_lang(self):
        course = CourseFactory(language='kg')
        courses_in_different_language = CourseFactory.create_many(
            CategoryFactory(course=None),
            TeacherFactory(course=None),
            language='ru'
        )
        path = reverse('course:course_list') + '?lang=kg'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['total'], 1)
        self.assert_equal_course(data['data'][0], course)

    def test_should_return_course_by_id(self):
        category = CategoryFactory(course=None)
        teacher = TeacherFactory(course=None)
        course = CourseFactory(category=category, teacher=teacher)
        path = reverse('course:course_detail', args=[course.id])

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assert_equal_course(data, course)
