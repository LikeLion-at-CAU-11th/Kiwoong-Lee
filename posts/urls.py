from django.urls import path, include
from posts.views import *
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('<int:id>/', post_detail, name="post_detail"),
#     path('new/', create_post, name="create_post"),
#     path('', get_post_all, name="get_post_all"),
#     path('comment/<int:post_id>/', get_comment, name='get_comment'),
#     path('',hello_world, name="hello_world"),
    # path('',PostList.as_view()),
    # path('<int:id>/',PostDetail.as_view()),
# ]

urlpatterns = [
    path('', PostListGenericAPIView.as_view()),
    path('<int:pk>/', PostDetailGenericAPIView.as_view()),
]

# router = DefaultRouter()
# router.register('',PostViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]