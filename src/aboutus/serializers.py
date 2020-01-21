from rest_framework.serializers import Serializer


class AboutUsSerializer(Serializer):
    def __init__(self, *args, lang=None,  **kwargs):
        self.lang = lang
        super(Serializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'payload': instance.payload_ru if instance.payload_ru and self.lang == 'ru' \
                else instance.payload_kg
        }
