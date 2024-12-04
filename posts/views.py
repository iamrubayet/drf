from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,APIView
from rest_framework import status,generics,mixins
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from accounts.serializers import CurrentUserPostsSerializer
from .permissions import ReadOnly,AuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
#this is not a api view. this is just a normal django way to take http request and give http response
# def homepage(request: HttpResponse):
#     response = {"message": "Hello World"}
#     return JsonResponse(data=response)

#data
# posts = [
#     {
#         "id": 1,
#         "title": "something",
#         "content": "something to be",

#     },
#     {
#         "id": 2,
#         "title": "something",
#         "content": "something to be",

#     }
# ]


###################--------------------------------this is function based view------------------------------------------------#############################################
class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = "page"
    page_size_query_param = "page_size"


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data
        response = {"message": "Hello World", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK)


# @api_view(http_method_names=["GET","POST"])
# def list_posts(request: Request):
#     posts = Post.objects.all() # this will return all the posts from the database or model

#     if request.method == "POST":
#         data = request.data
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "Post created successfully",
#                 "data": serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         response = {
#             "message": "Post not created",
#             "data": serializer.errors
#         }
#         return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
#     serializer = PostSerializer(instance=posts,many=True)

#     response ={
#         "message": "List of all posts",
#         "data": serializer.data

#     }
#     return Response(data=response, status=status.HTTP_200_OK)


# # #this is a api view for post detail
# @api_view(http_method_names=["GET"])
# def post_detail(request: Request, post_id: int):
#     post = get_object_or_404(Post, pk=post_id)
#     serializer = PostSerializer(instance=post)
#     response = {
#         "message": "Post detail",
#         "data": serializer.data
#     }
#     return Response(data=response, status=status.HTTP_200_OK)

  

# # @api_view(http_method_names=["PUT"])
# def update_post(request:Request,post_id:int):
#     post = get_object_or_404(Post,pk=post_id)
#     data = request.data
#     serializer = PostSerializer(instance=post,data=data)
#     if serializer.is_valid():
#         serializer.save()
#         response = {
#             "message": "Post updated successfully",
#             "data": serializer.data
#         }
#         return Response(data=response, status=status.HTTP_200_OK)
#     response = {
#         "message": "Post not updated",
#         "data": serializer.errors
#     }
#     return Response(data=response, status=status.HTTP_400_BAD_REQUEST)




# # @api_view(http_method_names=["DELETE"])
# def delete_post(request:Request,post_id:int):
#     post = get_object_or_404(Post,pk=post_id)
#     post.delete()
#     response = {
#         "message": "Post deleted successfully"
#     }
#     return Response(data=response, status=status.HTTP_200_OK)


###############t############this is the class view of it#####################################################################################

# class PostListCreateView(APIView):
#     """
#     This is a class based view for listing and creating posts
#     """
#     serializer_class = PostSerializer

#     def get(self,request:Request,*args,**kwargs):
#         posts = Post.objects.all()
#         serializer = self.serializer_class(instance=posts,many=True)
#         response ={
#             "message": "List of all posts",
#             "data": serializer.data

#         }
#         return Response(data=response, status=status.HTTP_200_OK)


#     def post(self,request:Request,*args,**kwargs):
#         data = request.data
#         serializer = self.serializer_class(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "Post created successfully",
#                 "data": serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
    

# class PostRetrieveUpdateDelete(APIView):
#     serializer_class = PostSerializer

#     def get(self,request:Request,post_id:int):
#         post = get_object_or_404(Post,pk=post_id)
#         serializer = self.serializer_class(instance=post)
#         response = {
#             "message": "Post detail",
#             "data": serializer.data
#         }
#         return Response(data=response, status=status.HTTP_200_OK)


#     def put(self,request:Request,post_id:int):
#         post = get_object_or_404(Post,pk=post_id)
#         data = request.data
#         serializer = self.serializer_class(instance=post,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "Post updated successfully",
#                 "data": serializer.data
#             }
#             return Response(data=response, status=status.HTTP_200_OK)
#         response = {
#             "message": "Post not updated",
#             "data": serializer.errors
#         }
#         return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request:Request,post_id:int):
#         post = get_object_or_404(Post,pk=post_id)
#         post.delete()
#         response = {
#             "message": "Post deleted successfully"
#         }
#         return Response(data=response, status=status.HTTP_200_OK)
    
#############--------------------------------this is a class view------------------------------------------------#############################################
    

###############################---------------this is for generic view and model mixins-------------------------------------------------#############################################




class PostListCreateView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = PostSerializer
    # permission_classes = [ReadOnly] #custom permission
    # permission_classes = [IsAuthenticated] #token or jwt
    permission_classes = [IsAuthenticatedOrReadOnly] #token or jwt
    pagination_class = CustomPaginator
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)
    @swagger_auto_schema(
            operation_summary="List all posts",
    )
    def get(self,request:Request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    @swagger_auto_schema(
            operation_summary="Creates a posts",
    )
    def post(self,request:Request,*args,**kwargs):
        return self.create(request,*args,**kwargs)





class PostRetrieveUpdateDelete(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AuthorOrReadOnly] #only the token or jwt of the author of the content can update or delete the content

    queryset = Post.objects.all()


    def get(self,request:Request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    
    def put(self,request:Request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request:Request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
def get_posts_for_current_user(request:Request):
    user = request.user
    serializer = CurrentUserPostsSerializer(instance=user,context={"request":request})
    return Response(data=serializer.data,status=status.HTTP_200_OK)

# query set filter starts here
class ListPostsForAuthor(generics.GenericAPIView,mixins.ListModelMixin):
   
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        # user = self.request.user
        # username = self.kwargs.get('username')
        username = self.request.query_params.get('username') or None
        queryset = Post.objects.all()
        if username is not None:
            return Post.objects.filter(author__username=username)
        return queryset
            
        

        

    def get(self,request:Request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    




###############----------------this is a short cut---------------#############################################################
