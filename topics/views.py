from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from topics.models import Topic, Resource
from topics.serializers import TopicSerializer, ResourceSerializer


class TopicBaseAPIView:
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Topic.objects.filter(owner=self.request.user)



class TopicListCreateAPIView(TopicBaseAPIView, generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class TopicDetailAPIView(TopicBaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    pass



class ResourceBaseAPIView:
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Resource.objects.select_related('topic').filter(topic__owner=self.request.user)


class ResourceListCreateAPIView(ResourceBaseAPIView, generics.ListCreateAPIView):
    pass

class ResourceDetailAPIView(ResourceBaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    pass