from django.contrib import admin

from topics.models import Resource, Topic


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'type', 'status', 'topic')
    list_filter = ('type', 'status')
    search_fields = ('title', 'url')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color', 'owner')
    list_filter = ('owner',)
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
