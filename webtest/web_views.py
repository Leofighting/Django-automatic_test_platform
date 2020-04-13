from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from webtest.models import WebCase, WebCaseStep


@login_required
def web_case_manage(request):
    web_case_list = WebCase.objects.all()
    username = request.session.get("user", "")
    return render(request, "web_case_manage.html", {
        "user": username,
        "web_cases": web_case_list
    })


@login_required
def web_case_step_manage(request):
    web_case_step_list = WebCaseStep.objects.all()
    username = request.session.get("user", "")
    return render(request, "web_case_step_manage.html", {
        "user": username,
        "web_case_steps": web_case_step_list
    })


@login_required
def web_search(request):
    username = request.session.get("user", "")
    search_webcasename = request.GET.get("webcasename", "")
    webcase_list = WebCase.objects.filter(web_case_name__icontains=search_webcasename)
    return render(request, "web_case_manage.html", {
        "user": username,
        "webcases": webcase_list
    })


@login_required
def web_step_search(request):
    username = request.session.get("user", "")
    search_webcasename = request.GET.get("webcasename", "")
    web_case_step_list = WebCaseStep.objects.filter(web_case_name__icontains=search_webcasename)
    return render(request, "web_case_step_manage.html", {
        "user": username,
        "webcasesteps": web_case_step_list
    })