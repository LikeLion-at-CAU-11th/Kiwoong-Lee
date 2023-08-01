#from rest_framework.serializers import ModelSerializer 
from rest_framework import serializers
from .models import Post #.현재 디렉토리 ..부모디렉토리 현재 디렉토리(posts)의 모델에서 Post model import

#ModelSerializer는 BaseSerializer를 상속받기에, 우리는 BS가 아닌 MS만 사용
class PostSerializer(serializers.ModelSerializer): #serialize할 모델명을 대문자로 적어주고 뒤에 Serializer붙여주기

  class Meta:
		# 어떤 모델을 시리얼라이즈할 건지
    model = Post
		# 모델에서 어떤 필드를 가져올지
		# 전부 가져오고 싶을 때
    fields = "__all__" #보편적으로 이걸 쓴다, 모든 필드를 시리얼라이즈(직렬화)하겠다.
		
	# 추가
		# 가져올 필드를 list 형태로 지정해줄 수도 있다.
		# fields = ['writer', 'content'] 
        # post와 content는 직렬화안됨.

		# 제외할 필드를 지정해줄 수도 있다.		
		# exclude = ['id']

		# create, update, delete는 안되고 read만 되는 필드를 선언할 수도 있다.(이름같이 변경되지 않아야하는 필드의 경우)
		# read_only_fields = ['writer']