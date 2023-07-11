from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Post, Comment
import json

from .serializers import PostSerializer 
from rest_framework.views import APIView
'''
1. APIView : 기본적인 클래스 뷰, http 메소드 별로 로직을 함수로 구현
2. GenericAPIView : 1을 상속받은 뷰 클래스, 단독 사용보단 concrete generic view 나 mixin과 결합하여 사용 
        *mixins : 반복적으로 serializer 사용 안하도 되게 다 구현되어 있음 (queryset, serializer 해야 함) 
        *concrete generic views : 상속받아야 하는게 넘 많아서 하나로 (queryset, serializer 해야 함)
3. ViewSet : 헬퍼클래스
        *ReadOnlyModelViewSet : 특정 레코드 조회용, 속도 빨라짐
        *ModelViewSet : 다른것도 해야할 때
        '''
from rest_framework.response import Response
from rest_framework import status #상태코드, 500번대는 BE문제/400번대는 FE문제
from django.http import Http404

#######인가구현 로그인한 사용자가 글 작성을 할 수 있도록, 로그인 안한 사용자는 읽기만 가능하게
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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

class PostList(APIView): #게시글 모델을 class형 view로 만듦, 이름이 중요하다! Post의 List를 담당하는 class의 코드   
    #새로운 게시글 만드는 메소드 (통상 PostDetail이 아닌 List에 생성하더라 ~ )
    
    #authentication_classes = [] 다음 시간에
    ##########인가구현
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    def post(self, request, format=None): 
        serializer = PostSerializer(data = request.data) #요청받은 data의 데이터를 data에 저장 후, 직렬화하는 과정
        if serializer.is_valid(): #유효한 값을 받았을 때의 분기점 생성
            # 역질렬화 과정이 필요할 때 유효성 검사가 필요
            # create, update
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #모든 게시글 가져오는 메소드
    def get(self, request, format=None): 
        posts = Post.objects.all() #쿼리셋 방식으로 모든 게시글 받아오기
        #serializer를 활용하니까 일일이 받아올 필요 없이 다음과 같은 코드로 ㄱㄱ
        serializer = PostSerializer(posts, many=True) #다중 값을 가져올 때 사용함
        return Response(serializer.data)
 
class PostDetail(APIView):
    def get(self, request, id):
        post = get_object_or_404(post, id=id) #get ~는 2개의 파라미터가 필요
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    #put은 전체 내용을 바꾸는 것, patch는 일부만 (패딩 패치 생각)
    def put(self, request, id):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        post = get_object_or_404(post, id=id) #각 CRUD에서 다 post 가져오고 시작
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import mixins
from rest_framework import generics
#전체
class PostListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
#단일객체
class PostDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

######################genericsAPIView

class PostListGenericAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 
class PostDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


####################viewset
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# post_list = PostViewSet.as_view({
#     'get' : 'list',
#     'post' : 'create',    
# })

# post_detail_vs = PostViewSet.as_view({
#     'get' : 'retrieve',
#     'put' : 'update',
#     'patch': 'partial_update',
#     'delete' : 'destroy'
# })

