from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from aboutus.models import AboutUs


class AboutUsAdmin(SummernoteModelAdmin):
    pass


admin.site.register(AboutUs, AboutUsAdmin)
