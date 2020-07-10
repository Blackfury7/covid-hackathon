from django.urls import path
from . import views


urlpatterns=[

path('registration/', views.user_registration, name="user_basics"),
path('details/', views.user_details, name="user_details"),
path('list/', views.user_list, name="user_list"),


	


]