from django.urls import path
from posts.views import *

urlpatterns = [
    path('', hello_world, name = 'hello_world'),
    path('introduction/', code_reviewer_info, name = 'code_reviewer_info'),
    path('post_detail/<int:id>/', get_post_detail),
    path('post_all/', get_post_all),
]