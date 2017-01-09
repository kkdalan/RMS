# _*_ coding: utf-8 _*_

from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.db.models import Max
from Issue.models import Issue, IssueForm

def edit_issue(request,issue_no):
    old_issue = Issue.objects.get(no = issue_no)
    if request.method == 'POST':
        form = IssueForm(request.POST, instance = old_issue)
        if form.is_valid():
            new_issue = form.save(commit=False)
            new_issue.save()
    form = IssueForm(instance = old_issue)
    return render(request,'issue_editor.html', {'form': form})

def new_issue(request):
    all = Issue.objects.all()
    max_no = all.aggregate(Max('no'))
    if request.method == 'POST':
        form = IssueForm(request.POST)
        new_issue = form.save(commit=False)
        if form.is_valid():
            # new_issue = issue.objects.create()
            # new_issue.no = max_no['no__max'] + 1
            new_issue.save()
    form = IssueForm()
    return render(request,'issue_editor.html', {'form': form})

# Create your views here.
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

def save_issue(request,new_issue):
    try:
        template = get_template('issue_list.html')
        new_issue.save()
        return HttpResponse(html)
    except:
        target_url = '/notfound/'
        return redirect(target_url)

def add_issue(request):
    try:
        template = get_template('issue_editor.html')
        all = Issue.objects.all()
        max_no = all.aggregate(Max('no'))
        new_issue = Issue.objects.create()
        new_issue.no = max_no + 1
        html = template.render(locals())
        return HttpResponse(html)
    except:
        target_url = '/notfound/'
        return redirect(target_url)

def create_issue(request,issue_no):
    try:
        template = get_template('issue_editor.html')
        old_issue = Issue.objects.get(no = issue_no)
        new_issue = old_issue
        html = template.render(locals())
        return HttpResponse(html)
    except:
        target_url = '/notfound/'
        return redirect(target_url)

def del_issue(request, issue_no):
    try:
        template = get_template('issue_editor.html')
        old_issue = Issue.objects.get(no = issue_no)
        old_issue.status = 'canceled'
        new_issue = old_issue
        new_issue.save()
        # html = template.render(locals())
        # return HttpResponse(html)
        target_url = '/list/all'
        return redirect(target_url)

    except:
        target_url = '/notfound/'
        return redirect(target_url)

def notfound(request, issue_no):
    template = get_template('notfound.html')
    now = datetime.now
    html = template.render(locals())
    return HttpResponse(html)


