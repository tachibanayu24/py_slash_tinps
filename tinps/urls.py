from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.show, name='show'),
    path('detail/', views.detail, name='detail'),
]
