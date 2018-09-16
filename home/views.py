from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
from post.models import Tinps


def index(request):
    context = {
        'tinps_list':Tinps.objects.all(),
        'user_list': User.objects.all(),
    }
    return render(request, 'index/index.html', context)


def about(request):
    context = {
        'tinps_list':Tinps.objects.all(),
        'user_list': User.objects.all(),
    }
    return render(request, 'about/index.html', context)
