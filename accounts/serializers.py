# accounts/serializers.py
from rest_framework_simplejwt.serializers import RefreshToken
from rest_framework import serializers
from .models import Member

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    username = serializers.CharField(required=True) #그냥 id라 해버리면 , 고유의 값이 id로 매겨지는데, 그거랑 혼동될 수 있음
    email = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)

    class Meta:
        model = Member
        fields = ['id', 'password', 'username', 'email', 'age'] #id와 username이 따로따로 있는거 확인, id는 자동으로 부여됨

    #회원정보 저장
    def save(self, request):
        member = Member.objects.create(
            username = self.validated_data['username'], #is_valid()가 호출되었을 때 유효성 검증을 통과한 값들을 넣어줌
            email=self.validated_data['email'],
            age=self.validated_data['age'],
        )
        # password 암호화
        member.set_password(self.validated_data['password'])
        member.save()

        return member
    
    #중복 방지
    def validate(self,data):
        email = data.get('email', None)
        username = data.get('username', None)

        if Member.objects.filter(email=email).exists():
            raise serializers.ValidationError('email already exists')
        if Member.objects.filter(username=username).exists():
             raise serializers.ValidationError('username already exists')
        
        return data
    
#로그인/로그아웃   
class AuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = Member
        fields = ['username', 'password']

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
				
		# Member DB에서 요청한 username과 일치하는 데이터가 존재하는지 확인
        if Member.objects.filter(username=username).exists():
             member = Member.objects.get(username=username)

        # DB에 데이터는 존재하지만 password가 불일치
             if not member.check_password(password):
                raise serializers.ValidationError("wrong password")
        
        else:
            raise serializers.ValidationError("member account not exist")
        
        token = RefreshToken.for_user(member)
        refresh_token = str(token)
        access_token = str(token.access_token)

        data = {
            'member' : member,
            'refresh_token' : refresh_token,
            'access_token' : access_token,
        }

        return data
