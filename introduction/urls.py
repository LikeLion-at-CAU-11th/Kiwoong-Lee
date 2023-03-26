from django.urls import path
from introduction.views import *

urlpatterns = [
    path('introduction', code_reviewer_info, name = 'code_reviewer_info'),
]