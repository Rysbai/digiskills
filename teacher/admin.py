from django.contrib import admin

from teacher.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    fields = ('name', 'surname', 'language', 'about_ru', 'about_kg', 'image', 'image_tag')


admin.site.register(Teacher, TeacherAdmin)
