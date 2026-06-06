from django.urls import path, include
from topics import views


urlpatterns = [
    path('', views.TopicListCreateAPIView.as_view(), name='topics'),
    path('<int:pk>/', views.TopicDetailAPIView.as_view(), name='topic' ),
]