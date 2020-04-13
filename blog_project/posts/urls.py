from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('',PostList.as_view()),
    path('users/',UserList.as_view()),
    path('users/<int:pk>/',UserDetail.as_view()),
]