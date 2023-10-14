from rest_framework import serializers
from .models import Category, Post, PostStatus


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        def create(self, validated_data):
            return Post(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

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

