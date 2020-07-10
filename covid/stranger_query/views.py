from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from . models import query



def ask_query(request):
	if request.method=="POST":
		data=json.loads(request.body)
		print(data)
		query.objects.create(**data)

	return JsonResponse("success",safe=False)

def pending_query(request):
	if request.method=="GET":
		
		message=list(query.objects.filter(status="pending").values())

	return JsonResponse(message,safe=False)

def reply_query(request):
	if request.method=="POST":
		data=json.loads(request.body)
		query_id=data['id']
		print(data)
		query.objects.filter(id=query_id).update(**data,status="verified")

	return JsonResponse("success",safe=False)

def verified_query(request):
	if request.method=="GET":
		
		message=list(query.objects.filter(status="verified").values())

	return JsonResponse(message,safe=False)