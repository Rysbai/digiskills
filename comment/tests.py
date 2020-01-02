from rest_framework import status
from unittest import mock
from django.test import TestCase
from factory import DjangoModelFactory

from comment.models import Comment
from comment.serializers import CommentSerializers
from comment import utils


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    name = 'Example name'
    phone = 'Example phone'
    text = 'Example text'
    available = True

    @staticmethod
    def create_many(count=3):
        comments = []
        for i in range(count):
            comments.append(CommentFactory())
        return comments


class CommentAPITest(TestCase):
    def test_should_return_list_of_all_comments(self):
        path = '/api/comments/'
        comments = CommentFactory.create_many()

        response = self.client.get(path)
        body = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body, CommentSerializers(comments, many=True).data)

    def test_should_create_comment(self):
        path = '/api/comments/'
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

    def test_should_send_mail_to_admin(self):
        path = '/api/comments/'
        data = {
            'name': 'Example name',
            'phone': '+996779583738',
            'text': 'Some comments here'
        }
        utils.send_comment_to_admin_email = mock.Mock(return_value=None)
        self.client.post(path, data=data, content_type='application/json')

        utils.send_comment_to_admin_email.assert_called_once()


