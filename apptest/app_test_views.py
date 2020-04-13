from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apptest.models import AppCase, AppCaseStep


@login_required
def app_case_manage(request):
    """
    app 用例管理
    :param request:
    :return: 跳转到app用例管理页面
    """
    app_case_list = AppCase.objects.all()
    username = request.session.get("user", "")
    return render(request, "app_case_manage.html", {
        "user": username,
        "app_cases": app_case_list
    })


@login_required
def app_case_step_manage(request):
    username = request.session.get("user", "")
    app_case_step_list = AppCaseStep.objects.all()
    return render(request, "app_case_step_manage.html", {
        "user": username,
        "app_case_steps": app_case_step_list
    })


@login_required
def apptest_report(request):
    username = request.session.get("user", "")
    return render(request, "apptest_report.html")


@login_required
def app_search(request):
    username = request.session.get("user", "")
    search_appcasename = request.GET.get("appcasename", "")
    appcase_list = AppCase.objects.filter(app_case_name__icontains=search_appcasename)
    return render(request, "app_case_manage.html", {
        "user": username,
        "appcases": appcase_list
    })


@login_required
def app_step_search(request):
    username = request.session.get("user", "")
    search_appcasename = request.GET.get("appcasename", "")
    appcasestep_list = AppCaseStep.objects.filter(app_case__app_case_name__icontains=search_appcasename)
    return render(request, "app_case_step_manage.html", {
        "user": username,
        "appcasesteps": appcasestep_list
    })