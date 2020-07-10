
from django.urls import path
from . import views


urlpatterns=[

path('create/', views.log_create, name="log_create"),
path('details/', views.log_details, name="log_details")

]



