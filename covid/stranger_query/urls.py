from django.urls import path
from . import views


urlpatterns=[

path('ask_query/', views.ask_query, name="ask_query"),
path('reply_query/', views.reply_query, name="reply_query"),
path('pending_query/', views.pending_query, name="pending_query"),
path('verified_query/', views.verified_query, name="success_query"),


	


]