from rest_framework import serializers

from topics.models import Topic, Resource


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', 'description', 'color', 'owner')
        read_only_fields = ('owner',)


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'title', 'url', 'type', 'status', 'topic')

    def validate_topic(self, value):
        user = self.context['request'].user

        if user != value.owner:
            raise serializers.ValidationError('Error')

        return value