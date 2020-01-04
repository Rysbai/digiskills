from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from aboutus.views import AboutUsView

app_name = 'aboutus'
urlpatterns = [
    path('', AboutUsView.as_view(), name='aboutus')
]

urlpatterns = format_suffix_patterns(urlpatterns)
