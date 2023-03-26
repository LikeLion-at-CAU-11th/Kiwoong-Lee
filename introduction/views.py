from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.

def code_reviewer_info(request):
    if request.method == "GET":
        return JsonResponse({
            'status' : 200,
	        'success' : True,
	        'message' : '메시지 전달 성공!!',
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