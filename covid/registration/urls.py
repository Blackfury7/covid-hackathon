from django.urls import path
from . import views


urlpatterns=[

path('user/', views.user_registration, name="user_registration"),
path('requests/', views.registration_requests, name="registration_requests"),
path('reply/', views.registration_reply, name="registration_reply"),
# path('verified/', views.registration_verified, name="registration_verified"),
# path('manager/', views.manager_registration, name="manager_registration"),


	


]