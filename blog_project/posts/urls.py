from django.urls import path
from .views import PostList, PostDetail

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('',PostList.as_view()),
]