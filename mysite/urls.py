"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Issue.views import login, index, add_issue, edit_issue, del_issue, notfound, issue_list

urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$',index),
    url(r'^list/(\w+)$',issue_list),
    url(r'^notfound/',notfound),
    url(r'^issue/add$',add_issue),
    url(r'^issue/edit/(\d+)$',edit_issue),
    url(r'^issue/del/(\d+)$',del_issue),
]
