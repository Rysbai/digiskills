from rest_framework.serializers import Serializer


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
            'image': instance.image.url,
            'views': instance.views,
            'available': instance.available
        }
