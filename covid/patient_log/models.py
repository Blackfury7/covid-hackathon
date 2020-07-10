from django.db import models
from user_basic_details . models import user_basics

class log(models.Model):

	user=models.ForeignKey(user_basics,null=True,on_delete=models.SET_NULL)
	
	status= models.CharField(max_length =20,default="pending")
	
	# request_status= models.CharField(max_length =20,default="Active")
	day= models.IntegerField()
	body= models.CharField(max_length = 2000)
	reject_reason= models.CharField(max_length = 500,blank=True)
	