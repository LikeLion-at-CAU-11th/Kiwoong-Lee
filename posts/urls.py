from django.urls import path, include
from posts.views import *

from rest_framework.routers import DefaultRouter
'''
urlpatterns = [
    # path('', hello_world, name = 'hello_world'),
    # path('introduction/', code_reviewer_info, name = 'code_reviewer_info'),
    # path('post_detail/<int:id>/', post_detail),
    # path('post_all/', get_post_all),
    # path('post_new/', create_post, name="create_post"), #라우팅
    # path('comment/<int:id>/', get_comment, name = 'get_comment'),
    # path('comment_new/<int:id>/', create_comment, name="create_comment")
    
    #APIView
    #path('', PostList.as_view()),
    #path('<int:id>/', PostDetail.as_view()) #요청을 id라는 int형 변수에 담아서 url mapping, 각 요청에 맞는 함수 body 실행
   
    #mixins
    #path('',PostListMixins.as_view()),
    #path('<int:pk>/', PostDetailMixins.as_view())

    #genericsAPIView
    #path('',PostListGenericAPIView.as_view()),
    #path('<int:pk>/', PostDetailGenericAPIView.as_view())

    #ViewSet
    # path('',post_list),
    # path('<int:pk>/', post_detail_vs)

    

]
'''
router = DefaultRouter()
router.register('', PostViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('',PostList.as_view()),
]