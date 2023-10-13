from django.contrib import admin
from django.urls import path
from .views import CategoryList, CategoryDetail


urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<slug:id>', CategoryDetail.as_view(), name='categories detail'),
]
