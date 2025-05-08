from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.create_post, name='create_post'),

    path('activity/', views.create_activity, name='post_activity'),

    path('posts_page/', views.posts_page, name='posts_page'),
]