from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Post


#week3_standard
def hello_world(request):
    if request.method == "GET":
        return JsonResponse({
            'status' : 200,
            'success' : True,
            'message' : '메시지 전달 성공!',
            'data' : "Hello world",
        })

#week3_challenge
def code_reviewer_info(request):
    if request.method == "GET":
        return JsonResponse({
            'status' : 200,
            'success' : True,
            'message' : '3주차 미션 성공!',
            'data' : [
            {
                "name" : "이기웅",
                "age" : 24,
                "major" : "Energy System Engineering"

            },
            {
                "name" : "박소은",
                "age" : 23,
                "major" : "Computer Science and Engineering"
            }
            ]
        })

#weeek4_standard   
@require_http_methods(["GET"]) 
def get_post_detail(request, id):
    post = get_object_or_404(Post, pk = id)
    category_json={
        "id"    : post.post_id,
        "writer": post.writer,
        "content": post.content,
        "category" : post.category,
    }
    return JsonResponse({
        'status' : 200,
        'message' : '게시글 조회 성공',
        'data' : category_json
    })

#week4_challenge
@require_http_methods(["GET"]) 
def get_post_all(request):
    posts = Post.objects.all()
    postList = []
    
    for post in posts:
        postList.append({
        "id"    : post.post_id,
        "writer": post.writer,
        "content": post.content,
        "category" : post.category,
    })
        
    return JsonResponse({
        'status' : 200,
        'message' : '게시글 조회 성공',
        'data' : postList
    })
