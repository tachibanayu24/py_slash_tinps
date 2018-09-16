from django.shortcuts import render

def mypage(request):
    return render(request, 'mypage/index.html')


def register(request):
    return render(request, 'register/index.html')
