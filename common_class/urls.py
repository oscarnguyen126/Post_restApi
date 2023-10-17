from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('countries/', views.CountryList.as_view(), name='countries'),
    path('countries/<slug:id>', views.CountryDetail.as_view(), name='countries_detail'),
    path('languages/', views.LanguageList.as_view(), name='language'),
    path('languages/<slug:id>', views.LanguageDetail.as_view(), name='language_detail'),
]
