from django.db import models


class news(models.Model):

	
	title = models.CharField(max_length =500)
	status= models.CharField(max_length =20,default="Active")
	body= models.CharField(max_length = 2000)
	url= models.CharField(max_length = 2000)