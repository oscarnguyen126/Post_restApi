from django.contrib import admin
from .models import PostStatus, Category, Post


admin.site.register(Post),
admin.site.register(Category),
admin.site.register(PostStatus),