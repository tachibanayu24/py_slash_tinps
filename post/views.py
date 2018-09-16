from django.shortcuts import render
from django.http import HttpResponse

def post(request):
    return render(request, 'post/index.html')


def edit(request):
    return render(request, 'edit/index.html')
