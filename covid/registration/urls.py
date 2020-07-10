from django.urls import path
from . import views


urlpatterns=[

path('user/', views.user_registration, name="user_registration"),
# path('manager/', views.manager_registration, name="manager_registration"),


	


]