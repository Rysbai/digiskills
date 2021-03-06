from unittest import skip

from django.core.exceptions import ValidationError
from django.urls import reverse
from rest_framework import status
from django.test import TestCase

from aboutus.factory import AboutUsFactory


class AboutUsAPITest(TestCase):
    def test_should_return_about_us_content_in_kyrgyz_by_default(self):
        aboutus = AboutUsFactory()
        path = reverse('aboutus:aboutus_list')

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['payload'], aboutus.payload_kg)

    def test_should_return_about_us_content_in_russian_with_query_param_lang(self):
        aboutus = AboutUsFactory()
        path = reverse('aboutus:aboutus_list') + '?lang=ru'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['payload'], aboutus.payload_ru)
