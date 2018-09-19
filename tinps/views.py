from django.shortcuts import render
from user.models import User
from post.models import Tinps, User

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

    tinps_id = request.GET.get('tinps_id')
    tinps = Tinps.objects.filter(tinps_id=tinps_id).first()

    #for item in tinps.user_name:
    user = User.objects.filter(user_id=tinps.user_name.user_id).first()
    print(user)

    print(vars(user))
    print("----------------------")
    context = {
        'tintin':tinps,
        'user':user,
    }
    print(context)
    return render(request, 'detail/index.html', context)
