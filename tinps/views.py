from django.shortcuts import render
#from users.models import Users
from users.models import CustomUser
from post.models import Tinps


def show(request):
    context = {
        'tinps_list':Tinps.objects.all(),
        'user_list': CustomUser.objects.all(),
        'tinps_list_order':Tinps.objects.all().order_by('-slashed_cnt'),
        # 'tinps_list_group' : Tinps.objects.select_related().all().aggregate(Slashed_cnt=sum('slashed_cnt'))
        'tinps_list_timeorder':Tinps.objects.all().order_by('-updated_at')
    }
    return render(request, 'show/index.html', context)


def detail(request):

    tinps_id = request.GET.get('tinps_id')
    tinps = Tinps.objects.filter(tinps_id=tinps_id).first()
    user = CustomUser.objects.filter(id=tinps.user.id).first()

    context = {
        'tintin':tinps,
        'user':user,
    }
    return render(request, 'detail/index.html', context)
