import pymysql
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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
    paginator = Paginator(apitest_list, 5)
    page = request.GET.get("page")
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


@login_required
def test_report(request):
    username = request.session.get("user", "")
    apis_list = Apis.objects.all()
    apis_count = Apis.objects.all().count()
    db = pymysql.connect(user="root", db="automatic", passwd="123qwe", host="127.0.0.1")
    cursor = db.cursor()
    sql1 = "select count(id) from apitest_apis where apitest_apis.api_status=1"
    aa = cursor.execute(sql1)
    apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]

    sql2 = "select count(id) from apitest_apis where apitest_apis.api_status=0"
    bb = cursor.execute(sql2)
    apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    db.close()
    return render(request, "report.html", {
        "user": username,
        "apiss": apis_list,
        "apiscounts": apis_count,
        "apis_pass_counts": apis_pass_count,
        "apis_fail_counts": apis_fail_count
    })


def left(request):
    return render(request, "left.html")


@login_required
def api_search(request):
    username = request.session.get("user", "")
    search_apitestname = request.GET.get("apitestname", "")
    apitest_list = ApiTest.objects.filter(apitest_name__icontains=search_apitestname)
    return render(request, "apitest_manage.html", {
        "user": username,
        "apitests": apitest_list
    })


@login_required
def apis_search(request):
    username = request.session.get("user", "")
    search_apiname = request.GET.get("apiname", "")
    apis_list = Apis.objects.filter(api_name__icontains=search_apiname)
    return render(request, "apis_manage.html", {
        "user": username,
        "apiss": apis_list
    })
