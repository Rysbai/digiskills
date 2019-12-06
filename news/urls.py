from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from news.views import NewsView

urlpatterns = [
    path('', NewsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
