from django.db import models


class query(models.Model):

	
	
	name= models.CharField(max_length = 100)
	status= models.CharField(max_length =20,default="pending")
	title= models.CharField(max_length = 200)
	is_fake= models.CharField(max_length = 50,blank=True)
	body= models.CharField(max_length = 2000)
	reply= models.CharField(max_length = 2000,blank=True)
	url= models.CharField(max_length = 1000,blank=True)
	reply_url= models.CharField(max_length = 1000,blank=True)
