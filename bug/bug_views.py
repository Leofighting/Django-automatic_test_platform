from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
    paginator = Paginator(bug_list, 5)
    page = request.GET.get("page", 1)
    currentPage = int(page)
    try:
        bug_list = paginator.page(currentPage)
    except PageNotAnInteger:
        bug_list = paginator.page(1)
    except EmptyPage:
        bug_list = paginator.page(paginator.num_pages)
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
