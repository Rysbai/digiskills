from django.test import TestCase
from django.urls import reverse

from news.factories import NewsFactory
from news.models import News
from utils.get_absolute_url import get_media_absolute_url


class NewsAPITest(TestCase):
    def assert_equal_kyrgyz_news(self, body: dict, news_orm: News):
        self.assertEqual(body['id'], news_orm.id)
        self.assertEqual(body['title'], news_orm.title_kg)
        self.assertEqual(body['description'], news_orm.description_kg)
        # self.assertEqual(body['image'], get_media_absolute_url(news_orm.image.url))
        # self.assertEqual(body['pub_date'], news_orm.pub_date)

    def assert_equal_russian_news(self, body: dict, news_orm: News):
        self.assertEqual(body['id'], news_orm.id)
        self.assertEqual(body['title'], news_orm.title_ru)
        self.assertEqual(body['description'], news_orm.description_ru)
        # self.assertEqual(body['image'], get_media_absolute_url(news_orm.image.url))
        # self.assertEqual(body['pub_date'], news_orm.pub_date)

    def test_should_return_max_10_last_added_news_by_default(self):
        NewsFactory.create_many(count=11)
        news = News.objects.all()
        path = reverse('news:news_list')

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['total'], len(news))
        self.assertEqual(len(data['data']), 10)

    def test_should_return_content_in_kyrgyz_language_by_default(self):
        NewsFactory.create_many(count=11)
        news = News.objects.all()
        path = reverse('news:news_list')

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        for i in range(len(data['data'])):
            self.assert_equal_kyrgyz_news(data['data'][i], news[i])

    def test_should_return_content_in_specific_language_i_want(self):
        NewsFactory.create_many(count=11)
        news = News.objects.all()
        path = reverse('news:news_list') + '?lang=ru'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        for i in range(len(data['data'])):
            self.assert_equal_russian_news(data['data'][i], news[i])

    def test_should_return_page_and_count_of_news_i_want(self):
        page, count = 1, 5
        NewsFactory.create_many(
            count=(page + 1) * count - 1 #for create -1 course for second page
        )
        news = News.objects.all()
        path = reverse('news:news_list') + '?page={0}&count={1}'.format(page, count)

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['total'], len(news))
        self.assertEqual(len(data['data']), len(news) - count)

    def test_should_return_news_by_id_in_kyrgyz_content_by_default(self):
        news = NewsFactory()
        path = reverse('news:news_detail', args=[news.id])

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assert_equal_kyrgyz_news(data, news)

    def test_should_return_news_by_id_in_language_i_want(self):
        news = NewsFactory()
        path = reverse('news:news_detail', args=[news.id]) + '?lang=ru'

        response = self.client.get(path)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assert_equal_russian_news(data, news)

    def test_should_return_404_if_news_doesnt_exist(self):
        doesnt_exist_news_id = 1234567
        path = reverse('news:news_detail', args=[doesnt_exist_news_id])

        response = self.client.get(path)

        self.assertEqual(response.status_code, 404)
