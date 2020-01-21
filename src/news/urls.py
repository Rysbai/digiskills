from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from news.views import NewsListView, NewsDetailView

app_name = 'news'
urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
