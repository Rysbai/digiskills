from django import forms
from django.core.exceptions import ValidationError

from news.models import News


class NewsForm(forms.ModelForm):
    title_kg = forms.CharField(required=False)
    title_ru = forms.CharField(required=False)

    def clean(self):
        title_kg = self.cleaned_data.get('title_kg', None)
        title_ru = self.cleaned_data.get('title_ru', None)
        description_kg = self.cleaned_data.get('description_kg', None)
        description_ru = self.cleaned_data.get('description_ru', None)

        if not title_kg and not title_ru:
            raise ValidationError('Пожалуйста заполните поле ЗАГОЛОВОК НОВОСТЯ хотя бы на русском или на кургызском.')
        if not description_kg and not description_ru:
            raise ValidationError('Пожалуйста заполните поле ОПИСАНИЕ НОВОСТЯ хотя бы на русском или на кургызском.')
        return self.cleaned_data

    class Meta:
        model = News
        fields = (
            'title_kg',
            'title_ru',
            'description_kg',
            'description_ru',
            'image',
            'pub_date',
            'views',
        )
