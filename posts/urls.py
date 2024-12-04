from . import views

from django.urls import path

#patterns
urlpatterns = [
    path("homepage/", views.homepage, name="posts_home"),
    path("", views.PostListCreateView.as_view(), name="lists_post"),
    path("<int:pk>/", views.PostRetrieveUpdateDelete.as_view(), name="post_detail"),
    path("current_user/", views.get_posts_for_current_user, name="current_user_posts"),
    # path("posts_for/<username>", views.ListPostsForAuthor.as_view(), name="posts_for_current_user"),
    path("posts_for/", views.ListPostsForAuthor.as_view(), name="posts_for_current_user"),
   
    
]



# from . import views

# from django.urls import path

# #patterns
# urlpatterns = [
#     path("homepage/", views.homepage, name="posts_home"),
#     path("", views.PostListCreateView.as_view(), name="lists_post"),
#     path("<int:post_id>/", views.PostRetrieveUpdateDelete.as_view(), name="post_detail"),
   
    
# ]
