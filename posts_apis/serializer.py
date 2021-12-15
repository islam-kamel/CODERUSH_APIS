from rest_framework import serializers

from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    create_by = serializers.CurrentUserDefault

    class Meta:
        model = Posts
        fields = ['id', 'title', 'content', 'image', 'create_by', 'slug']
