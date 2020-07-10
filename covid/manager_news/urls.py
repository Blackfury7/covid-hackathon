from django.urls import path
from . import views


urlpatterns=[

path('create/', views.create_news, name="create_news"),
path('show/', views.show_news, name="show_news"),


	


]