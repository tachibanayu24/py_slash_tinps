from django.shortcuts import render
from .models import User
from post.models import Tinps

def mypage(request):
    #　本来はログイン中のユーザのみ渡すはず
    context = {
        'tinps_list':Tinps.objects.all(),
        'user_list': User.objects.all(),
    }
    return render(request, 'mypage/index.html', context)


def register(request):
    #　本来はログイン中のユーザのみ渡すはず
    context = {
        'tinps_list':Tinps.objects.all(),
        'user_list': User.objects.all(),
    }
    return render(request, 'register/index.html', context)

