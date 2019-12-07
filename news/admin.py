from django.contrib import admin

from news.models import News


class NewsAdmin(admin.ModelAdmin):
    summernote_fields = ('description_kg', 'description_ru')
    readonly_fields = ('image_tag',)
    fieldsets = (
        ("Название мероприятия", {
            'fields': ('title_kg', 'title_ru')
        }),
        ("Описание", {
            'fields': ('description_kg', 'description_ru')
        }),
        (None, {
            'fields': ('image', 'image_tag', 'available')
        })
    )


admin.site.register(News, NewsAdmin)
