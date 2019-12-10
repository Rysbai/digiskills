from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from news.models import News


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('description_kg', 'description_ru')
    readonly_fields = ('image_tag', 'views')
    list_display = ('__str__', 'views')
    fieldsets = (
        (None, {
            'fields': ('image', 'image_tag', 'views', 'pub_date')
        }),
        ("Название мероприятия", {
            'fields': ('title_kg', 'title_ru')
        }),
        ("Описание", {
            'fields': ('description_kg', 'description_ru')
        })
    )


admin.site.register(News, NewsAdmin)
