from django.urls import path
from .views import (index, about, add_post, post_list, post_detail)

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('posts/add', add_post, name='add_post'),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail')

]
