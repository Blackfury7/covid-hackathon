from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from user_basic_details . models import user_basics
from manager_basic_details . models import manager_basics



def user_login(request):
	if request.method=="POST":
		data=json.loads(request.body)
		username=data['username']
		password=data['password']
		print(data)
		user=user_basics.objects.filter(username=username,password=password)
		if user.exists():
			message=user[0].id
		else:
			message="invalid details"
		return JsonResponse(message,safe=False)

def manager_login(request):
	if request.method=="POST":
		data=json.loads(request.body)
		username=data['username']
		password=data['password']
		manager=manager_basics.objects.filter(username=username,password=password)
		if manager.exists():
			message=manager[0].id
		else:
			message="invalid details"
		return JsonResponse(message,safe=False)