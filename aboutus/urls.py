from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from aboutus.views import AboutUsView

urlpatterns = [
    path('', AboutUsView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
