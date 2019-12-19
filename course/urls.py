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
urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),

    path('teachers/', TeacherListView.as_view()),
    path('teachers/<int:pk>/', TeacherDetailView.as_view()),

    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>/', CourseDetailView.as_view()),

    path('programs/', ProgramItemView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
