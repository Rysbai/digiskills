from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/course/', include('course.urls')),
    path('api/news/', include('news.urls')),
    path('api/contacts/', include('contacts.urls')),
    path('api/aboutus/', include('aboutus.urls')),

    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
