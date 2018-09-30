from django.shortcuts import render
from users.models import CustomUser
from post.models import Tinps

def mypage(request):
    #　本来はログイン中のユーザのみ渡すはず
    user = request.user

    context = {
        'tinps_list':Tinps.objects.filter(user_id=user.id).all(),
        'user': user,
    }
    return render(request, 'mypage/index.html', context)


def register(request):
    #　本来はログイン中のユーザのみ渡すはず
    context = {
        'tinps_list':Tinps.objects.all(),
        'user_list': CustomUser.objects.all(),
    }
    return render(request, 'register/index.html', context)

