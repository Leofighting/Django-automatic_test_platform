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