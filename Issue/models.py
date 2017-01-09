# _*_ coding:utf-8 _*_

from __future__ import unicode_literals

from datetime import datetime, date
from django.db import models
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Issue(models.Model):
    no = models.AutoField(primary_key=True)
    topic = models.CharField(blank=True,max_length=20)
    desc = models.TextField(blank=True,max_length=255)
    notes = models.TextField(blank=True,max_length=255)
    type = models.CharField(blank=True,max_length=10)
    owner = models.CharField(blank=True,max_length=20)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    close_date = models.DateField(blank=True)
    status = models.CharField(blank=True,max_length=10)
    sys_time = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.topic

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'
        labels = {
                'no': _('編號'),
                'topic': _('主題'),
                'desc': _('問題描述'),
                'notes': _('備註'),
                'type': _('類型'),
                'owner': _('負責人'),
                'start_date': _('起始日'),
                'end_date': _('到期日'),
                'close_date': _('結案日'),
                'status': _('狀態'),
                'sys_time':_('系統時間'),
        }
        widgets = {
                'desc': Textarea(attrs={'cols': 100, 'rows': 5}),
                'notes': Textarea(attrs={'cols': 100, 'rows': 5}),
        }

