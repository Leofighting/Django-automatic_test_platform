from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from apitest.models import ApiTest, ApiStep, Apis


def test(request):
    return HttpResponse("hello test")


def login(request):
    """
    登陆功能
    :param request:
    :return: 成功则跳转到登陆页面
    """
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            request.session["user"] = username
            response = HttpResponseRedirect("/home/")
            return response
        else:
            return render(request, "login.html", {
                "error": "用户名 或 密码错误~"
            })
    return render(request, "login.html")


def home(request):
    """
    主页
    :param request:
    :return:登陆成功，跳转到主页面
    """
    return render(request, "home.html")


def logout(request):
    """
    退出登录
    :param request:
    :return: 跳转到登陆页面
    """
    auth.login(request)
    return render(request, "login.html")


@login_required
def apitest_manage(request):
    """
    接口管理
    :param request:
    :return: 跳转到接口管理页面，并输出所有接口用例
    """
    apitest_list = ApiTest.objects.all()
    username = request.session.get("user", "")
    return render(request, "apitest_manage.html", {
        "user": username,
        "apitests": apitest_list
    })


@login_required
def apistep_manage(request):
    username = request.session.get("user", "")
    apistep_list = ApiStep.objects.all()
    return render(request, "apistep_manage.html", {
        "user": username,
        "apisteps": apistep_list
    })


@login_required
def apis_manage(request):
    username = request.session.get("user", "")
    apis_list = Apis.objects.all()
    return render(request, "apis_manage.html", {
        "user": username,
        "apiss": apis_list
    })