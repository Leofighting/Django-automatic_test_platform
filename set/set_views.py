from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

from set.models import Set


def set_manage(request):
    """设置管理"""
    username = request.session.get("user", "")
    set_list = Set.objects.all()
    return render(request, "set_manage.html", {
        "user": username,
        "sets": set_list
    })


def set_user(request):
    """用户设置"""
    user_list = User.objects.all()
    username = request.session.get("user", "")
    return render(request, "set_user.html", {
        "user": username,
        "users": user_list
    })


@login_required
def set_search(request):
    username = request.session.get("user", "")
    search_setname = request.GET.get("setname", "")
    set_list = Set.objects.filter(set_name__icontains=search_setname)
    return render(request, "set_manage.html", {
        "user": username,
        "sets": set_list
    })


@login_required
def user_search(request):
    username = request.session.get("user", "")
    search_username = request.GET.get("username", "")
    user_list = User.objects.filter(username__icontains=search_username)
    return render(request, "set_user.html", {
        "user": username,
        "users": user_list
    })
