from django.contrib import admin

from tracking.models import Goal, StudySession


# Register your models here.
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('topic', 'target_minutes', 'deadline', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('topic__name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ('topic', 'date', 'duration_minutes', 'notes')
    list_filter = ('date',)
    search_fields = ('topic__name',)
    ordering = ('-created_at',)