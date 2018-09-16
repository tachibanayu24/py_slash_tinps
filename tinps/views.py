from django.shortcuts import render
from user.models import User
from post.models import Tinps


def show(request):
    context = {
        'tinps_list':Tinps.objects.all(),
        'user_list': User.objects.all(),
    }
    return render(request, 'show/index.html', context)


def detail(request):
    context = {
        'tinps_list':Tinps.objects.all(),
        'user_list': User.objects.all(),
    }
    return render(request, 'detail/index.html', context)
