from django.contrib import admin

from .models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_by')
    prepopulated_fields = {'slug': ('title',)}