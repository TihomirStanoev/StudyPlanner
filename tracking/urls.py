from django.urls import path
from tracking import views


sessions_urlpatterns = [
    path('', views.StudySessionListCreateAPIView.as_view(), name='sessions'),
    path('<int:pk>/', views.StudySessionDetailAPIView.as_view(), name='session')
]


goals_urlpatterns = [
    path('', views.GoalListCreateAPIView.as_view(), name='goals'),
    path('<int:pk>/', views.GoalDetailAPIView.as_view(), name='goal'),
]