from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from user_basic_details . models import user_basics



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

def manager_registration(request):
	if request.method=="POST":
		data=json.loads(request.body)
		username=data['username']
		email=data['email']
		phone_no=data['phone_no']
		print(data)
		# try:

		if manager_basics.objects.filter(username=username).exists():
		    message='This username is already taken'
		 
		elif manager_basics.objects.filter(email=email).exists():
		 
		    message='This email is already registered'
		elif user_basics.objects.filter(phone_no=phone_no).exists():
		 
		    message='This phone is already registered'

		else:

			manager_basics.objects.create(**data)


			message="You are successfully registered"

		# except: 
		# 	message="Error: Could not process your request"
		
		return JsonResponse(message,safe=False)