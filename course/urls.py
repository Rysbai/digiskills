from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from course.views import CategoryView, \
    TeacherView,\
    CourseView, \
    ScheduleView, \
    MaterialView, \
    ProgramItemView, \
    VideoLessonView

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:pk>/', CategoryView.as_view()),

    path('teachers/', TeacherView.as_view()),
    path('teachers/<int:pk>/', TeacherView.as_view()),

    path('courses/', CourseView.as_view()),
    path('courses/<int:pk>/', CourseView.as_view()),

    path('schedules/', ScheduleView.as_view()),
    path('materials/', MaterialView.as_view()),
    path('programs/', ProgramItemView.as_view()),
    path('video_lessons/', VideoLessonView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
