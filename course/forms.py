from django import forms
from django.core.exceptions import ValidationError

from course.models import Course, Material, VideoLesson


class CourseForm(forms.ModelForm):
    name_kg = forms.CharField(required=False)
    name_ru = forms.CharField(required=False)

    def clean(self):
        name_kg = self.cleaned_data.get('name_kg', None)
        name_ru = self.cleaned_data.get('name_ru', None)
        description_kg = self.cleaned_data.get('description_kg', None)
        description_ru = self.cleaned_data.get('description_ru', None)

        if not name_kg and not name_ru:
            raise ValidationError('Пожалуйста заполните поле НАЗВАНИЕ КУРСА хотя бы на русском или на кургызском.')
        if not description_kg and not description_ru:
            raise ValidationError('Пожалуйста заполните поле ОПИСАНИЕ КУРСА хотя бы на русском или на кургызском.')
        return self.cleaned_data

    class Meta:
        model = Course
        fields = (
            'category',
            'teacher',
            'language',
            'name_kg',
            'name_ru',
            'description_kg',
            'description_ru',
            'registration_link',
            'start',
            'end',
            'available'
        )


class MaterialForm(forms.ModelForm):
    description_kg = forms.CharField(required=False)
    description_ru = forms.CharField(required=False)

    def clean(self):
        description_kg = self.cleaned_data.get('description_kg', None)
        description_ru = self.cleaned_data.get('description_ru', None)

        if not description_kg and not description_ru:
            raise ValidationError('Пожалуйста заполните поле ОПИСАНИЕ МАТЕРИАЛА хотя бы на русском или на кургызском.')
        return self.cleaned_data

    class Meta:
        model = Material
        fields = (
            'description_kg',
            'description_ru',
            'link'
        )


class VideoLessonForm(forms.ModelForm):
    description_kg = forms.CharField(required=False)
    description_ru = forms.CharField(required=False)

    def clean(self):
        description_kg = self.cleaned_data.get('description_kg', None)
        description_ru = self.cleaned_data.get('description_ru', None)

        if not description_kg and not description_ru:
            raise ValidationError('Пожалуйста заполните поле ОПИСАНИЕ ВИДЕО хотя бы на русском или на кургызском.')
        return self.cleaned_data

    class Meta:
        model = VideoLesson
        fields = (
            'description_kg',
            'description_ru',
            'link'
        )
