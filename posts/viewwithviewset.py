from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Post
from posts.serializers import PostSerializer
from django.shortcuts import get_object_or_404



class PostViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        response = {
            "message": "List of all posts",
            "data": serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)



        

    def create(self, request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Post created successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {
            "message": "Post not created",
            "data": serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(Post,pk=pk)
        serializer = PostSerializer(post)
        response = {
            "message": "Post detail",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        post = get_object_or_404(Post,pk=pk)
        data = request.data
        serializer = PostSerializer(instance=post,data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Post updated successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        response = {
            "message": "Post not updated",
            "data": serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pass
        

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post,pk=pk)
        post.delete()
        response = {
            "message": "Post deleted successfully"
        }
        return Response(data=response, status=status.HTTP_204_NO_CONTENT)
    



class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    


