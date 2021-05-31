from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import DateInput
from django.shortcuts import render, redirect
from .forms import SubTaskForm
from django import forms
from django.views.generic import CreateView, UpdateView
from django.urls import reverse

from .models import Comment, Sprint, project
from .models import Task


# startTime = forms.DateField(widget=forms.SelectDateWidget)

class add_comment(CreateView, LoginRequiredMixin):
    model = Comment
    fields = '__all__'


class update_comment(UpdateView, LoginRequiredMixin):
    model = Comment
    fields = '__all__'


class add_task(CreateView, LoginRequiredMixin):
    model = Task
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['StartTime'] = forms.DateField(widget=forms.SelectDateWidget)
        return context


class update_task(UpdateView, LoginRequiredMixin):
    model = Task
    fields = '__all__'


class add_sprint(CreateView, LoginRequiredMixin):
    model = Sprint
    fields = '__all__'


class update_sprint(UpdateView, LoginRequiredMixin):
    model = Sprint
    fields = '__all__'


class add_project(CreateView, LoginRequiredMixin):
    model = project
    fields = '__all__'


class update_project(UpdateView, LoginRequiredMixin):
    model = project
    fields = '__all__'


class InputForm(forms.Form):
    work_done = forms.IntegerField(max_value=100, min_value=0)
