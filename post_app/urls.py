from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('categories/<slug:id>', views.CategoryDetail.as_view(), name='categories_detail'),
    path('poststatus/', views.PostStatusList.as_view(), name='post_status'),
    path('poststatus/<slug:id>', views.PostStatusDetail.as_view(), name='post_status_detail'),
    path('posts/', views.PostList.as_view(), name='post'),
    path('posts/<slug:id>', views.PostDetail.as_view(), name='post_detail'),
    path('search/', views.PostSearch.as_view(), name='search'),
]
