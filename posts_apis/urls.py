from django.urls import path

from .views import PostsListAPIView, PostDetailsAPIView

appname = 'posts_view'

urlpatterns = [
    path('posts/', PostsListAPIView.as_view(), name='posts-list'),
    path('posts/<str:slug>-<int:pk>/', PostDetailsAPIView.as_view(),
         name='post_details')
]
