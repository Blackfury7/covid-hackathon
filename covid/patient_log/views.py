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





