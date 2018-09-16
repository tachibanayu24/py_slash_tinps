from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Tinps


def post(request):
    context = {
        'tinps_list':Tinps.objects.all(),
    }
    return render(request, 'post/index.html', context)


def edit(request):
    context = {
        'tinps_list':Tinps.objects.all(),
    }
    return render(request, 'edit/index.html')
