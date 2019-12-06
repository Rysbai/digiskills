from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from teacher.views import TeacherView

urlpatterns = [
    path('', TeacherView.as_view()),
    path('<int:pk>', TeacherView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
