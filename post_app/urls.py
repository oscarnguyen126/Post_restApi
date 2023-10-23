from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Index, name='index'),
    path('create/', post_create, name='post_create'),
]

from .rest_urls import urlpatterns as HurlPatterns
urlpatterns.extend(HurlPatterns)