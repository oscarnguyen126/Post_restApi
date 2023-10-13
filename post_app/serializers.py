from rest_framework import serializers
from .models import Category, Post, PostStatus


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

        def create(self, validated_data):
            return Category(**validated_data)


class PostStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostStatus
        fields = '__all__'

        def create(self, validated_data):
            return PostStatus(**validated_data)

