from django.urls import path
from . import views

    #passar argumentos pala Url - str:name é um parametro usado no arquivo views
urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.tasklist, name='task-list')
    #path('yourname/<str:name>', views.yourame, name='yourname')
]
