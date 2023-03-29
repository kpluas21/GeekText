from django.urls import path 
from . import views
from django.conf import settings 

urlpatterns = [
    path('getUser/<str:username>/', views.getUser),
    path('userList/', views.getUserList),
    path('postUser/', views.createUser),
    path('updateUser/<str:username>/', views.updateUser),
    

    #path('postUser/, views.logIn),
]   