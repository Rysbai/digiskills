from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from comment.views import CommentViews

urlpatterns = [
    path('', CommentViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
