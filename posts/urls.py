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
    # path('',PostList.as_view()),
    # path('<int:id>/',PostDetail.as_view()),
# ]

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]

# urlpatterns = [
#     path('', post_list),
#     path('<int:pk>/', post_detail_vs)
#     path('', post_list),
#     path('<int:pk>/', post_detail_vs)
# ]



router = DefaultRouter()
router.register('', PostViewSet)

# router = DefaultRouter()
# router.register('',PostViewSet)
router.register('', PostViewSet)

# router = DefaultRouter()
# router.register('',PostViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
# urlpatterns = [
#     path('', include(router.urls)),
# ]