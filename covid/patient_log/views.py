from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from . models import log




def log_create(request):
	if request.method=="POST":
		data=json.loads(request.body)
		
		user_id=data['user_id']
		
		print(data)
		if log.objects.filter(user_id=user_id,day=data['day']).exists():
			log.objects.filter(user_id=user_id,day=data['day']).update(**data)
		else:
			log.objects.create(**data)


		return JsonResponse("success",safe=False)

def log_details(request):
	if request.method=="POST":
		data=json.loads(request.body)
		print(data)
		
		user_id=data['user_id']
		
		new_logs=list(log.objects.filter(user_id=user_id).order_by('day').values('id','user_id','user__name','day','body'))
		return JsonResponse(new_logs,safe=False)

def log_requests(request):
	if request.method=="GET":
		
		new_logs=list(log.objects.filter(status="pending").values('id','user_id','user__name','day','body'))
		return JsonResponse(new_logs,safe=False)


def log_reply(request):
	if request.method=="POST":
		data=json.loads(request.body)
		
		log_id=data['id']
		
		print(data)
		log.objects.filter(id=log_id).update(**data)

		return JsonResponse("success",safe=False)

def log_verified(request):
	if request.method=="GET":
		
		new_logs=list(log.objects.filter(status="accepted").values('id','user_id','user__name','day','body'))
		return JsonResponse(new_logs,safe=False)





