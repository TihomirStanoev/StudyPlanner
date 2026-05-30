from rest_framework import serializers

from tracking.models import StudySession, Goal


class StudySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySession
        fields = ('id', 'topic', 'date', 'duration_minutes', 'notes')


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'topic', 'target_minutes', 'deadline', 'is_completed')