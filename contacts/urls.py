from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from contacts.views import ContactView

urlpatterns = [
    path('', ContactView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
