from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.loginsite),
    path('register',views.registration),
    path('home',views.index),
    path('profile',views.profile),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
    
]
