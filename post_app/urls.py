from django.contrib import admin
from django.urls import path
from .views import CategoryList, CategoryDetail, PostStatusList, PostStatusDetail


urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<slug:id>', CategoryDetail.as_view(), name='categories detail'),
    path('poststatus/', PostStatusList.as_view(), name='post status'),
    path('poststatus/<slug:id>', PostStatusDetail.as_view(), name='post status detail'),
]
