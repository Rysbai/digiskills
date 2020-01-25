from django.conf import settings

PROTOCOL = 'https' if settings.MEDIA_SSL_SECURED else 'http'


def get_media_absolute_url(relative_path):
    return '%s://%s:%s%s' % (PROTOCOL, settings.MEDIA_HOST_NAME, settings.MEDIA_PORT, relative_path)
