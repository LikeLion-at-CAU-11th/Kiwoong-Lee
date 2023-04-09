from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Post, Comment
import json

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

#weeek4_standard + week5_standard
@require_http_methods(["GET","PATCH","DELETE"]) 
def post_detail(request, id): #애 안에 patch , delete 다 할꺼라 이름 변경
    if request.method == "GET": #if 문안에 들어가게 하단 내용 전부 tab
        post = get_object_or_404(Post, pk = id)
        
        post_json={
            "id"    : post.id,
            "writer": post.writer,
            "content": post.content,
            "category" : post.category,
        }
        return JsonResponse({
            'status' : 200,
            'message' : '게시글 조회 성공',
            'data' : post_json
        })
    
    elif request.method == "PATCH":
        body = json.loads(request.body.decode('utf-8')) #수정할 내용 body에 넣어서 전달
        update_post = get_object_or_404(Post, pk=id)

        update_post.content = body['content'] #모델 봤을 때 바꿀만한 내용은 body와 category 뿐
        update_post.category = body['category']
        update_post.save() #수정하고 저장하는 ORM, PATCH 동작을 할 때에 반드시 필요

        update_post_json = {
            "id": update_post.id,
            "writer": update_post.writer,
            "content": update_post.content,
            "category": update_post.category,
        }

        return JsonResponse({
            'status': 200,
            'message': '게시글 수정 성공',
            'data': update_post_json
        })
    
    elif request.method == "DELETE":
        delete_post = get_object_or_404(Post,pk=id)
        delete_post.delete()

        return JsonResponse({
            'status' : 200,
            'message' : '게시글 삭제 성공'
        })

#week4_challenge
@require_http_methods(["GET"]) 
def get_post_all(request):
    post_all = Post.objects.all() #Post 데이터베이스에 있는 모든 데이터를 불러와 queryset형식으로 저장

    post_json_all= [] #데이터를 json형식으로 변환하여 리스트에 저장
    for post in post_all:
        post_json= {
        "id"    : post.id,
        "writer": post.writer,
        "content": post.content,
        "category" : post.category,
        }
    post_json_all.append(post_json)
        
    return JsonResponse({
        'status' : 200,
        'message' : '게시글 조회 성공',
        'data' : post_json_all
    })

#week5_standard
@require_http_methods(["POST"])
def create_post(request): #받을 때에도 json형식으로
    body = json.loads(request.body.decode('utf-8'))
    #ORM을 통해서 새로운 데이터를 DB에 생성함
    new_post = Post.objects.create(
        writer = body['writer'],
        content = body['content'],
        category = body['category'],
    )

    # Response에서 보일 데이터 내용을 Json 형태로 예쁘게 만들어줌
    new_post_json = {
        "id" : new_post.id,
        "writer" : new_post.writer,
        "content" : new_post.content,
        "category" : new_post.category
    }

    return JsonResponse({
        'status' : 200,
        'message' : '게시글 생성 성공',
        'data' : new_post_json

    })

@require_http_methods(["GET"])
def get_comment(request, id):
    comment_all = Comment.objects.filter(post = id)
    comment_json_list = []

    for comment in comment_all:
        comment_json = {
            'writer' : comment.writer,
            'content' : comment.content
        }

        comment_json_list.append(comment_json)
    
    return JsonResponse({
        'status' : 200,
        'message' : "댓글 읽어오기 성공",
        'data' : comment_json_list
    })

@require_http_methods(["POST"])
def create_comment(request,id):
    body = json.loads(request.body.decode('utf-8'))

    new_comment = Comment.objects.create(
        writer = body['writer'],
        content = body['content'],
        post = Post.objects.get(pk=id)
    )

    new_comment_json = {
        "writer" : new_comment.writer,
        "content" : new_comment.content
    }

    return JsonResponse({
        'status' : 200,
        'message' : '댓글 생성 성공',
        'data' : new_comment_json
        })

       