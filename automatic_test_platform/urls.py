"""automatic_test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apitest import views
from apptest import app_test_views
from bug import bug_views
from product import pro_views
from set import set_views
from webtest import web_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("test/", views.test, name="test"),
    path("login/", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout, name="logout"),
    # 接口测试管理
    path("apitest_manage/", views.apitest_manage, name="apitest_manage"),
    path("apistep_manage/", views.apistep_manage, name="apistep_manage"),
    path("apis_manage/", views.apis_manage, name="apis_manage"),
    # 产品管理
    path("product_manage/", pro_views.product_manage, name="product_manage"),
    # bug 管理
    path("bug_manage/", bug_views.bug_manage, name="bug_manage"),
    # 设置管理
    path("set_manage/", set_views.set_manage, name="set_manage"),
    # 用户管理
    path("user/", set_views.set_user, name="user"),
    # app 用例管理
    path("app_case_manage/", app_test_views.app_case_manage, name="app_case_manage"),
    path("app_case_step_manage/", app_test_views.app_case_step_manage, name="app_case_step_manage"),
    # web 用例管理
    path("web_case_manage/", web_views.web_case_manage, name="web_case_manage"),
    path("web_case_step_manage/", web_views.web_case_step_manage, name="web_case_step_manage"),
]
