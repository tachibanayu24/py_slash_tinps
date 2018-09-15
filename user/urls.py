from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('mypage/', views.mypage, name='mypage'),
    path('register/', views.register, name='register'),
]
