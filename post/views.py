from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Tinps
from user.models import User
from .forms import TinpsForm
from django.conf.urls import url
from xml.dom.minidom import parseString
from django.contrib.auth.models import User
from django.contrib import messages


def post(request):
    context = {
        'tinps_list':Tinps.objects.all(),
        'form':TinpsForm()
    }
    return render(request, 'post/index.html', context)


def edit(request):
    context = {
        'tinps_list':Tinps.objects.all(),
    }
    return render(request, 'edit/index.html', context)


def insert(request):
    req = request.POST
    user = request.user
    vars(user)

    # tinps用
    title = req["title"]
    tinps_body = req["tinps_body"]
    query = Tinps(
        title=title,
        tinps_body=tinps_body.replace('\n||\r||\r\n', '<br>'),
        user=user,
        #category
    )
    query.save()
    messages.success(request, '新たなtinpsを投稿しました！！！')

    return redirect('/tinps/show')


def update(request):
    print (request.POST)
    # req = request.POST
    #
    # # ユーザ様
    # user = User(
    #     user_id="630552b028414439ad3a52c931781044",
    #     user_name="",
    #     mail="",
    #     pwd=""
    # )
    #
    # # tinps用
    # title = req["title"]
    # tinps_body = req["tinps_body"]
    #
    # #printtinps_body.replace('\n||\r||\r\n', '<br>')
    # query = Tinps(
    #     title=title,
    #     tinps_body=tinps_body.replace('\n||\r||\r\n', '<br>'),
    #     user_name=user,
    #     #category
    # )
    # query.save()
    #
    # # return redirect(request, 'show/index.html')
    return redirect(request, '/tinps/show/')




