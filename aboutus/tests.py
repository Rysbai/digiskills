from django.core.exceptions import ValidationError
from rest_framework import status
from django.test import TestCase
from factory import DjangoModelFactory

from aboutus.models import AboutUs


class AboutUsFactory(DjangoModelFactory):
    class Meta:
        model = AboutUs

    payload_kg = 'Example payload in kyrgyz'
    payload_ru = 'Example payload in russian'


class AboutUsModelTest(TestCase):
    def test_should_raise_validate_error_if_aboutus_already_exist(self):
        first = AboutUs.objects.create(payload_kg='First about us', payload_ru='First about us')
        second = AboutUs.objects.create(payload_kg='Second about us', payload_ru='Second about us')
        first.save()

        with self.assertRaises(ValidationError):
            second.save()


class AboutUsAPITest(TestCase):
    def test_should_return_about_us_content_in_kyrgyz_by_default(self):
        aboutus = AboutUsFactory()
        path = '/api/aboutus/'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['payload'], aboutus.payload_kg)

    def test_should_return_about_us_content_in_russian_with_query_param_lang(self):
        aboutus = AboutUsFactory()
        path = '/api/aboutus/?lang=ru'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['payload'], aboutus.payload_ru)
