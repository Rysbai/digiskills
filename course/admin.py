from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin
from django_summernote.utils import get_attachment_model
from django.contrib import admin
from django.contrib.auth.models import Group, User

from course.models import Course, \
    Teacher,\
    Category, \
    ProgramItem


class CategoryAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    list_display = ('__str__', )
    fields = ('name', 'surname', 'position', 'language', 'about_ru', 'about_kg', 'image', 'image_tag')


class ProgramItemInline(admin.StackedInline, SummernoteInlineModelAdmin):
    summernote_fields = '__all__'
    model = ProgramItem
    fk_name = 'course'


class CourseAdmin(SummernoteModelAdmin):
    summernote_fields = ''
    readonly_fields = ('image_tag', )
    fieldsets = (
        (None, {
            'fields': (
                'category',
                'teacher',
                'language',
                'image',
                'image_tag',
                'name',
                'description',
                'available',
                'isOnline'
            )
        }),
        ('Заполнить если курс онлайн.', {
            'fields': (
                'registration_link',
                'start',
                'link_to_video'
            )
        })
    )
    inlines = (
        ProgramItemInline,
    )


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(get_attachment_model())


admin.site.register(Category, CategoryAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
