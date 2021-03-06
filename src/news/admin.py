from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from news.models import News


class NewsAdmin(SummernoteModelAdmin):
    def image_tag(admin, obj):
        if obj.image:
            return mark_safe('<img src="/media/{}" width="50%", height="50%" >'.format(obj.image))
        return '-'
    image_tag.short_description = 'Изображение (соотношение 16:9)'
    image_tag.allow_tags = True

    summernote_fields = ('description_kg', 'description_ru')
    readonly_fields = ('image_tag', 'views')
    list_display = ('__str__', 'views')
    fieldsets = (
        (None, {
            'fields': ('image', 'image_tag', 'views', 'pub_date')
        }),
        ("Заголовок мероприятия", {
            'fields': ('title_kg', 'title_ru')
        }),
        ("Описание", {
            'fields': ('description_kg', 'description_ru')
        })
    )


admin.site.register(News, NewsAdmin)
