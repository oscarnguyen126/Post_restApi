from django.contrib import admin
from django.urls import path
from . import rest_views


urlpatterns = [
    path('categories/', rest_views.CategoryList.as_view(), name='categories'),
    path('categories/<slug:id>', rest_views.CategoryDetail.as_view(), name='categories_detail'),
    path('poststatus/', rest_views.PostStatusList.as_view(), name='post_status'),
    path('poststatus/<slug:id>', rest_views.PostStatusDetail.as_view(), name='post_status_detail'),
    path('posts/', rest_views.PostList.as_view(), name='post'),
    path('posts/<slug:id>', rest_views.PostDetail.as_view(), name='post_detail'),
    path('search/', rest_views.PostSearch.as_view(), name='search'),
]
