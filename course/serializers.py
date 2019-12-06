from rest_framework import serializers

from course.models import Category,\
    Course, \
    ProgramItem,\
    Material,\
    VideoLesson,\
    ScheduleItem
from teacher.models import Teacher


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category.id'
    )
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        source='teacher.id'
    )

    class Meta:
        model = Course
        fields = (
            'id',
            'category_id',
            'teacher_id',
            'name_kg',
            'name_ru',
            'description_kg',
            'description_ru',
            'image',
            'registration_link',
            'start',
            'end'
        )


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


class MaterialSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course.id'
    )

    class Meta:
        model = Material
        fields = ('id', 'course_id', 'description_kg', 'description_ru', 'link')


class VideoLessonSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course.id'
    )

    class Meta:
        model = VideoLesson
        fields = ('id', 'course_id', 'description_kg', 'description_ru', 'link')
