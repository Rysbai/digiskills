from rest_framework import serializers
from rest_framework.serializers import Serializer

from course.models import \
    Course, \
    ProgramItem

from utils.get_absolute_url import get_media_absolute_url


class CategorySerializer(Serializer):
    def __init__(self, *args, lang=None, **kwargs):
        self.lang = lang
        super(Serializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name_ru if instance.name_ru and self.lang == 'ru' else instance.name_kg
        }


class TeacherSerializer(Serializer):
    def __init__(self, *args, lang=None,  **kwargs):
        self.lang = lang
        super(Serializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        if self.lang == 'ru':
            about = instance.about_ru or instance.about_kg
        else:
            about = instance.about_kg or instance.about_ru
        return {
            'id': instance.id,
            'name': instance.name,
            'surname': instance.surname,
            'position': instance.position,
            'about': about,
            'image': get_media_absolute_url(instance.image.url),
            'language': instance.language
        }


class CourseSerializer(Serializer):

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'category_id': instance.category_id,
            'category_name': instance.category.name_kg if instance.language == 'kg' else instance.category.name_ru,
            'teacher_id': instance.teacher_id,
            'language': instance.language,
            'name': instance.name,
            'description': instance.description,
            'image': get_media_absolute_url(instance.image.url),
            'isOnline': instance.isOnline,
            'registration_link': instance.registration_link,
            'start': instance.start,
            'link_to_video': instance.link_to_video,
            'available': instance.available
        }


class ProgramItemSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course.id'
    )

    class Meta:
        model = ProgramItem
        fields = ('id', 'course_id', 'number', 'title', 'content')
