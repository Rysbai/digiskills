from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
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
    def image_tag(admin, obj):
        if obj.image:
            return mark_safe('<img src="/media/{}" width="50%", height="50%" >'.format(obj.image))
        return '-'

    image_tag.short_description = 'Изображение (соотношение 1:1)'
    image_tag.allow_tags = True

    readonly_fields = ('image_tag',)
    list_display = ('__str__', )
    fields = ('name', 'surname', 'position', 'language', 'about_ru', 'about_kg', 'image', 'image_tag')


class ProgramItemInline(admin.StackedInline, SummernoteInlineModelAdmin):
    summernote_fields = '__all__'
    model = ProgramItem
    fk_name = 'course'


class CourseAdmin(SummernoteModelAdmin):
    def image_tag(admin, obj):
        if obj.image:
            return mark_safe('<img src="/media/{}" width="50%", height="50%" >'.format(obj.image))
        return '-'

    image_tag.short_description = 'Изображение (соотношение 16:9)'
    image_tag.allow_tags = True

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
admin.site.unregister(get_attachment_model())
admin.site.site_header = _("Администрирование Digital Skills")
admin.site.site_title = _("Администрирование Digital Skills")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)

