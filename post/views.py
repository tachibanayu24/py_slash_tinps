from django.shortcuts import render
from django.http import HttpResponse

def post(request):
    return HttpResponse("<h1>#post</h1>")


def edit(request):
    return HttpResponse("<h1>#edit</h1>")
