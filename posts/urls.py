from django.urls import path
from posts.views import *

urlpatterns = [
    path('', hello_world, name = 'hello_world'),
    path('introduction/', code_reviewer_info, name = 'code_reviewer_info'),
]