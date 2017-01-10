# _*_ coding: utf-8 _*_

from django.shortcuts import render, redirect
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.db.models import Max
from Issue.models import Issue, IssueForm

# Create your views here.
def login(request):
    template = get_template('login.html')
    try:
        user_id = request.GET('user_id')
        user_pass = request.GET('user_pass')
    except:
        user_id = None
    if user_id != None and user_pass == '0000':
        verified = True
    else:
        verified = False
    html = template.render(locals())
    return HttpResponse(html)

def index(request):
    template = get_template('index.html')
    now = datetime.now
    html = template.render(locals())
    return HttpResponse(html)

def issue_list(request, criteria ):
    template = get_template('issue_list.html')
    if criteria == 'all':
        all = Issue.objects.all()
    else:
        all = Issue.objects.filter(status = criteria)
    now = datetime.now
    html = template.render(locals())
    return HttpResponse(html)

def add_issue(request):
    all = Issue.objects.all()
    max_no = all.aggregate(Max('no'))
    new_no = max_no['no__max'] + 1
    # old_issue = Issue.objects.create(no = new_no)
    if request.method == 'POST':
        issue_form = IssueForm(request.POST)
        if issue_form.is_valid():
            msg = "您的案件已儲存！"
            new_issue = issue_form.save(commit=False)
            new_issue.no = new_no
            new_issue.save()
            return HttpResponseRedirect('/list/all')
        else:
            msg = "欄位驗證錯誤！"
    else:
        issue_form = IssueForm()
        new_issue = issue_form.save(commit=False)
        new_issue.no = new_no
    template = get_template('issue_editor.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

def edit_issue(request,issue_no):
    old_issue = Issue.objects.get(no = issue_no)
    if request.method == 'POST':
        issue_form = IssueForm(request.POST, instance = old_issue)
        if issue_form.is_valid():
            msg = "您的案件已儲存！"
            new_issue = issue_form.save()
            return HttpResponseRedirect('/list/all')
        else:
            msg = "欄位驗證錯誤！"
    else:
        issue_form = IssueForm(instance = old_issue)
        new_issue = issue_form.save(commit=False)
    template = get_template('issue_editor.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

def del_issue(request, issue_no):
    old_issue = Issue.objects.get(no = issue_no)
    old_issue.delete()
    return HttpResponseRedirect('/list/all')

def notfound(request, issue_no):
    template = get_template('notfound.html')
    now = datetime.now
    html = template.render(locals())
    return HttpResponse(html)


