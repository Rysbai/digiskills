from django_summernote.admin import SummernoteModelAdmin
from django_summernote.utils import get_attachment_model
from django.contrib import admin
from django.contrib.auth.models import Group, User

from course.forms import CourseForm, MaterialForm, VideoLessonForm
from course.models import Course, \
    Teacher,\
    Category, \
    ProgramItem, \
    Material, \
    VideoLesson, \
    ScheduleItem


class ProgramItemInline(admin.TabularInline):
    model = ProgramItem
    fk_name = 'course'


class ScheduleItemInline(admin.TabularInline):
    model = ScheduleItem
    fk_name = 'course'


class MaterialsInline(admin.TabularInline):
    form = MaterialForm
    model = Material
    fk_name = 'course'


class VideoLessonsInline(admin.TabularInline):
    form = VideoLessonForm
    model = VideoLesson
    fk_name = 'course'


class CategoryAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    list_display = ('__str__', )
    fields = ('name', 'surname', 'position', 'language', 'about_ru', 'about_kg', 'image', 'image_tag')


class CourseAdmin(SummernoteModelAdmin):
    form = CourseForm
    summernote_fields = ''
    readonly_fields = ('image_tag', )
    fieldsets = (
        (None, {
            'fields': (
                'category', 'teacher', 'language',
                'image', 'image_tag', 'registration_link', 'start', 'end'
            )
        }),
        ("Название курса", {
            'fields': ('name_kg', 'name_ru')
        }),
        ("Описание курса", {
            'fields': ('description_kg', 'description_ru')
        })
    )
    inlines = (
        ProgramItemInline,
        ScheduleItemInline,
        MaterialsInline,
        VideoLessonsInline
    )


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(get_attachment_model())


admin.site.register(Category, CategoryAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
