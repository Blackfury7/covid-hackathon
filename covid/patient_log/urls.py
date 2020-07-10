
from django.urls import path
from . import views


urlpatterns=[

path('create/', views.log_create, name="log_create"),
path('requests/', views.log_requests, name="log_requests"),
path('details/', views.log_details, name="log_details"),
path('reply/', views.log_reply, name="log_reply"),
# path('verified/', views.log_verified, name="log_verified"),


]



