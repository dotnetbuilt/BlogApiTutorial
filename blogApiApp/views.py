from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import status

@api_view(['GET'])
def index(request):
    return Response({"Success":"The setup was successful"})

@api_view(['GET'])
def get_all_posts(request):
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def create_post(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"The post was successfully created"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"Success":"The post was successfully deleted"}, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response({"Error":"The post does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_post(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response({"Error":"The post does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update_post(request):
    post_id = request.data.get('post_id')
    new_title = request.data.get('title')
    new_content = request.data.get('content')
    try:
        post = Post.objects.get(id=post_id)
        if new_title:
            post.title = new_title
        if new_content:
            post.content = new_content
        post.save()
        return Response({"Success":"The post was successfully updated"}, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response({"Error":"The post does not exist"}, status=status.HTTP_404_NOT_FOUND)      