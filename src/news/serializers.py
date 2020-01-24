from rest_framework.serializers import Serializer

from utils.get_absolute_url import get_media_absolute_url


class NewsSerializer(Serializer):
    def __init__(self, *args, lang=None,  **kwargs):
        self.lang = lang
        super(Serializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        if self.lang == 'ru':
            title = instance.title_ru or instance.title_kg
            description = instance.description_ru or instance.description_kg
        else:
            title = instance.title_kg or instance.title_ru
            description = instance.description_kg or instance.description_ru

        return {
            'id': instance.id,
            'title': title,
            'description': description,
            'image': get_media_absolute_url(instance.image.url),
            'views': instance.views,
            'pub_date': instance.pub_date
        }
