from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from bug.models import Bug


def bug_manage(request):
    """
    bug 管理
    :param request:
    :return: 跳转到 bug 管理页面
    """
    username = request.session.get("user", "")
    bug_list = Bug.objects.all()
    return render(request, "bug_manage.html", {
        "user": username,
        "bugs": bug_list
    })


@login_required
def bug_search(request):
    username = request.session.get("user", "")
    search_bugname = request.GET.get("bugname", "")
    bug_list = Bug.objects.filter(bug_name__icontains=search_bugname)
    return render(request, "bug_manage.html", {
        "user": username,
        "bugs": bug_list
    })
