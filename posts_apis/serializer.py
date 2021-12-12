from rest_framework import serializers

from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Posts
        fields = ['id', 'title', 'content', 'image', 'create_by', 'slug']
