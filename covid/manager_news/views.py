from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from . models import news



def create_news(request):
	if request.method=="POST":
		data=json.loads(request.body)
		
		print(data)
		news.objects.create(**data)
		message="success"

	return JsonResponse(message,safe=False)
def show_news(request):
	if request.method=="GET":
		
		message=list(news.objects.all().values())
		

	return JsonResponse(message,safe=False)