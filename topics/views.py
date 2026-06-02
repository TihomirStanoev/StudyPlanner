from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from topics.models import Topic
from topics.serializers import TopicSerializer


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