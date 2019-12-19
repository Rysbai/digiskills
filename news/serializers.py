from rest_framework.serializers import Serializer

from utils.get_absolute_url import get_absolute_url


class NewsSerializer(Serializer):
    def __init__(self, *args, lang=None,  **kwargs):
        self.lang = lang
        super(Serializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title_ru if instance.title_ru and self.lang == 'ru' else instance.title_kg,
            'description': instance.description_ru if instance.description_ru and self.lang == 'ru' \
                else instance.description_kg,
            'image': get_absolute_url(instance.image.url),
            'views': instance.views,
            'pub_date': instance.pub_date
        }
