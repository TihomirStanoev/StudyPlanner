from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from tracking.models import StudySession, Goal
from tracking.serializers import StudySessionSerializer, GoalSerializer


class StudySessionBaseAPIView:
    serializer_class = StudySessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudySession.objects.select_related('topic').filter(topic__owner=self.request.user)


class StudySessionListCreateAPIView(StudySessionBaseAPIView, generics.ListCreateAPIView):
    pass


class StudySessionDetailAPIView(StudySessionBaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    pass


class GoalBaseAPIView:
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Goal.objects.select_related('topic').filter(topic__owner=self.request.user)




class GoalListCreateAPIView(GoalBaseAPIView, generics.ListCreateAPIView):
    pass


class GoalDetailAPIView(GoalBaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    pass