from rest_framework import serializers
from rest_framework.serializers import Serializer

from course.models import \
    Course, \
    ProgramItem,\
    ScheduleItem


class CategorySerializer(Serializer):
    def __init__(self, *args, lang=None, **kwargs):
        self.lang = lang
        super(Serializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name_ru if instance.name_ru and self.lang == 'ru' else instance.name_kg
        }


class CourseSerializer(Serializer):
    def __init__(self, *args, lang=None, **kwargs):
        self.lang = lang
        super(Serializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'category_id': instance.category_id,
            'teacher_id': instance.teacher_id,
            'name': instance.name_ru if instance.name_ru and self.lang == 'ru' else instance.name_kg,
            'description': instance.description_ru if instance.description_ru and self.lang == 'ru' \
                else instance.description_kg,
            'image': instance.image.url,
            'registration_link': instance.registration_link,
            'start': instance.start,
            'end': instance.end
        }


class ScheduleItemSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course.id'
    )

    class Meta:
        model = ScheduleItem
        fields = ('id', 'course_id', 'day', 'time')


class ProgramItemSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course.id'
    )

    class Meta:
        model = ProgramItem
        fields = ('id', 'course_id', 'title')


class MaterialSerializer(Serializer):
    def __init__(self, *args, lang=None, **kwargs):
        self.lang = lang
        super(Serializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'course_id': instance.course_id,
            'description': instance.description_ru if instance.description_ru and self.lang == 'ru' \
                else instance.description_kg,
            'link': instance.link
        }


class VideoLessonSerializer(Serializer):
    def __init__(self, *args, lang=None, **kwargs):
        self.lang = lang
        super(Serializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'course_id': instance.course_id,
            'description': instance.description_ru if instance.description_ru and self.lang == 'ru' \
                else instance.description_kg,
            'link': instance.link
        }
