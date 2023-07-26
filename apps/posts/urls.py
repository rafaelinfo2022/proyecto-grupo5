from django.urls import path
from .views import PostListView
from .views import PostListView, PostDetailView
#from .views import posts

app_name ='apps.posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post_individual')
]