from rest_framework import serializers

from posts.models import Post
from .models import Post


#plain serializer
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=50)
#     content = serializers.CharField(max_length=500)
#     created = serializers.DateTimeField(read_only=True)

#model serializer
#fields and meta are required for model serializer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created']
