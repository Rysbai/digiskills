from django.contrib import admin

from news.models import News


class NewsAdmin(admin.ModelAdmin):
    summernote_fields = ''
    readonly_fields = ('image_tag',)
    fieldsets = (
        (None, {
            'fields': ('image', 'image_tag', 'date')
        }),
        ("Название мероприятия", {
            'fields': ('title_kg', 'title_ru')
        }),
        ("Описание", {
            'fields': ('description_kg', 'description_ru')
        }),
        ("Место проведения", {
            'fields': ('location_kg', 'location_ru')
        }),
    )


admin.site.register(News, NewsAdmin)
