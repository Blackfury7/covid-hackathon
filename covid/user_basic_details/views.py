from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from . models import user_basics



def user_registration(request):
	if request.method=="POST":
		data=json.loads(request.body)
		username=data['username']
		email=data['email']
		phone_no=data['phone_no']
		print(data)
		# try:

		if user_basics.objects.filter(username=username).exists():
		    message='This username is already taken'
		 
		elif user_basics.objects.filter(email=email).exists():
		 
		    message='This email is already registered'
		elif user_basics.objects.filter(phone_no=phone_no).exists():
		 
		    message='This phone is already registered'

		else:

			user_basics.objects.create(**data)


			message="You are successfully registered"

		# except: 
		# 	message="Error: Could not process your request"
		
		return JsonResponse(message,safe=False)

def user_details(request):
	if request.method=="POST":
		data=json.loads(request.body)
		id=data['id']
		print(data)
		details=list(user_basics.objects.filter(id=id,status="accept").values('id','name','username','address','gender','email','phone_no','dob','blood_group'))
		return JsonResponse(details,safe=False)

def user_list(request):
	if request.method=="GET":
		usr_list=list(user_basics.objects.filter(status='accept').values('id','name','username','address','gender','email','phone_no','dob','blood_group'))
		return JsonResponse(usr_list,safe=False)


