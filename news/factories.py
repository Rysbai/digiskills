import datetime
import factory

from news.models import News


class NewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = News

    title_kg = 'Example title in kyrgyz'
    title_ru = 'Example title in russian'
    description_kg = 'Example description in kyrgyz'
    description_ru = 'Example description in russian'
    image = factory.django.ImageField(filename='image.png')
    views = 1
    pub_date = datetime.datetime.now()

    @staticmethod
    def create_many(count=3):
        news = []
        for i in range(count):
            news.append(NewsFactory())
        return news
