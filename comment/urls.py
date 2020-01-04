from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from comment.views import CommentViews

app_name = 'comment'
urlpatterns = [
    path('', CommentViews.as_view(), name='comment_list_and_create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
