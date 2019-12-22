from django.urls import path
from . import views
from .views import (
    PostListView,PostDetailView,PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    )
urlpatterns = [
    # path('', views.home , name='test-home'),
    path('', PostListView.as_view(), name='test-home'),
    path('home/', PostListView.as_view(), name='test-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about , name='test-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
