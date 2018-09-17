from django.shortcuts import render
from user.models import User
from post.models import Tinps


def show(request):
    context = {
        'tinps_list':Tinps.objects.all(),
        'user_list': User.objects.all(),
        'tinps_list_order':Tinps.objects.all().order_by('-slashed_cnt'),
        # 'tinps_list_group' : Tinps.objects.select_related().all().aggregate(Slashed_cnt=sum('slashed_cnt'))
        'tinps_list_timeorder':Tinps.objects.all().order_by('-updated_at')
    }
    return render(request, 'show/index.html', context)


def detail(request):
    context = {
        'tinps_list':Tinps.objects.all(),
        'user_list': User.objects.all(),
    }
    return render(request, 'detail/index.html', context)
