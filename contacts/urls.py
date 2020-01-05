from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from contacts.views import ContactView

app_name = 'contact'
urlpatterns = [
    path('', ContactView.as_view(), name='contact_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
