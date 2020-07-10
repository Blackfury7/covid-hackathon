from django.db import models


class manager_basics(models.Model):

	
	name = models.CharField(max_length =50)
	status= models.CharField(max_length =20,default="Active")
	username= models.CharField(max_length = 50)
	gender= models.CharField(max_length =20,blank=True)
	blood_group= models.CharField(max_length = 50)
	password= models.CharField(max_length = 50)
	phone_no= models.CharField(max_length =20)
	email= models.CharField(max_length =50)
	address= models.CharField(max_length =200,blank=True)
	dob= models.CharField(max_length =20,blank=True)
	


