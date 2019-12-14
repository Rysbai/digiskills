from django.contrib import admin

from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'phone', 'text')
    fields = ('name', 'phone', 'text', 'available')


admin.site.register(Comment, CommentAdmin)
