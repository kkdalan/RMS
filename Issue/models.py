# _*_ coding:utf-8 _*_

from __future__ import unicode_literals

from datetime import datetime, date
from django.db import models
from django import forms
from functools import partial
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
    start_date = models.CharField(blank=True,max_length=10)
    end_date = models.CharField(blank=True,max_length=10)
    close_date = models.CharField(blank=True,max_length=10)
    status = models.CharField(blank=True,max_length=20)
    sys_time = models.DateTimeField(blank=True,default=datetime.now, editable = False)

    def __unicode__(self):
        return self.topic

class IssueForm(ModelForm):
    STATUS = [
        ['New','New'],
        ['Processing','Processing'],
        ['Rejected','Rejected'],
        ['Closed','Closed'],
    ]
    
    status = forms.ChoiceField(label='Status', choices=STATUS)

    class Meta:
        model = Issue
        fields = '__all__'
        labels = {
                'no': _('No'),
                'topic': _('Topic'),
                'desc': _('Description'),
                'notes': _('Notes'),
                'type': _('Type'),
                'owner': _('Owner'),
                'start_date': _('Start Date'),
                'end_date': _('End Date'),
                'close_date': _('Close Date'),
                'status': _('Status'),
                'sys_time':_('System Time'),
        }
        widgets = {
                'desc': Textarea(attrs={'cols': 50, 'rows': 5}),
                'notes': Textarea(attrs={'cols': 50, 'rows': 5}),
                'start_date': forms.DateInput(attrs={'class':'datepicker'}),
        }

