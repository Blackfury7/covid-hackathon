from django.urls import path
from . import views


urlpatterns=[

path('user/', views.user_login, name="user_login"),
path('manager/', views.manager_login, name="manager_login"),


	


]