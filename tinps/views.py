from django.shortcuts import render

def show(request):
    return render(request, 'show/index.html')


def detail(request):
    return render(request, 'detail/index.html')
