from django.urls import reverse
from rest_framework import status
from unittest import mock
from django.test import TestCase

from comment.serializers import CommentSerializers
from comment.factory import CommentFactory


class CommentAPITest(TestCase):
    def test_should_return_list_of_all_comments(self):
        path = reverse('comment:comment_list_and_create')
        comments = CommentFactory.create_many()

        response = self.client.get(path)
        body = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body, CommentSerializers(comments, many=True).data)

    def test_should_create_comment(self):
        path = reverse('comment:comment_list_and_create')
        data = {
            'name': 'Example name',
            'phone': '+996779583738',
            'text': 'Some comments here'
        }

        response = self.client.post(path, data=data, content_type='application/json')
        body = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(body['name'], data['name'])
        self.assertEqual(body['phone'], data['phone'])
        self.assertEqual(body['text'], data['text'])

    @mock.patch('comment.utils.send_comment_to_admin_email')
    def test_should_send_mail_to_admin(self, mocked_send_comment_to_admin_email):
        path = reverse('comment:comment_list_and_create')
        data = {
            'name': 'Example name',
            'phone': '+996779583738',
            'text': 'Some comments here'
        }
        self.client.post(path, data=data, content_type='application/json')

        mocked_send_comment_to_admin_email.assert_called_once()
