from rest_framework.serializers import ModelSerializer
from posts.models import Post


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'published_at',
            'user'
        ]


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'published_at',
            'slug',
            'user'
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'published_at',
            'slug',
            'user'
        ]