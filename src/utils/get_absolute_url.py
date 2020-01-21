from django.conf import settings

PROTOCOL = 'https' if settings.SSL_SECURED else 'http'


def get_media_absolute_url(relative_path):
    return '%s://%s:%s%s' % (PROTOCOL, settings.HOST_NAME, settings.PORT, relative_path)
