from django.contrib import admin

from news.models import News


class NewsAdmin(admin.ModelAdmin):
    summernote_fields = ('description_kg', 'description_ru')
    readonly_fields = ('image_tag',)
    fieldsets = (
        (None, {
            'fields': ('image', 'image_tag')
        }),
        ("Название мероприятия", {
            'fields': ('title_kg', 'title_ru')
        }),
        ("Описание", {
            'fields': ('description_kg', 'description_ru')
        }),
        (None, {
            'fields': ('available', )
        })
    )


admin.site.register(News, NewsAdmin)
