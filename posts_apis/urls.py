from django.urls import path

from .views import PostsListAPIView, PostDetailsAPIView

appname = 'posts_view'

urlpatterns = [
    path('posts/', PostsListAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailsAPIView.as_view())
]
