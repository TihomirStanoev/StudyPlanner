from django.urls import path
from topics import views


topics_urlpatterns = [
    path('', views.TopicListCreateAPIView.as_view(), name='topics'),
    path('<int:pk>/', views.TopicDetailAPIView.as_view(), name='topic' ),
]


resources_urlpatterns = [
    path('', views.ResourceListCreateAPIView.as_view(), name='resources'),
    path('<int:pk>/', views.ResourceDetailAPIView.as_view(), name='resource' ),
]