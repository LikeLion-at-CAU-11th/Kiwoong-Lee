from django.urls import path
from posts.views import *

urlpatterns = [
    path('', hello_world, name = 'hello_world'),
    path('introduction/', code_reviewer_info, name = 'code_reviewer_info'),
    path('post_detail/<int:id>/', post_detail),
    path('post_all/', get_post_all),
    path('post_new/', create_post, name="create_post"), #라우팅
    path('comment/<int:id>/', get_comment, name = 'get_comment'),
    path('comment_new/<int:id>/', create_comment, name="create_comment")
]