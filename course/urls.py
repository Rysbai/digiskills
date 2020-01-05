from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from course.views import (
CategoryListView,
CategoryDetailView,
TeacherListView,
TeacherDetailView,
CourseListView,
CourseDetailView,
ProgramItemView
)

app_name = 'course'
urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),

    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),

    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),

    path('programs/', ProgramItemView.as_view(), name='program_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
