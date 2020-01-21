from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/course/', include('course.urls', namespace='course')),
    path('api/news/', include('news.urls', namespace='news')),
    path('api/contacts/', include('contacts.urls', namespace='contact')),
    path('api/aboutus/', include('aboutus.urls', namespace='aboutus')),
    path('api/comments/', include('comment.urls', namespace='comment')),

    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
