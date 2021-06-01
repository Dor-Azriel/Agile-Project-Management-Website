from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.forms import DateInput
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SubTaskForm
from django import forms
from django.views.generic import CreateView, UpdateView
from django.urls import reverse

from .models import Comment, Sprint, project, SubTask
from .models import Task


# startTime = forms.DateField(widget=forms.SelectDateWidget)

class add_comment(CreateView, LoginRequiredMixin, ):
    model = Comment
    fields = '__all__'


    def get_initial(self, *args, **kwargs):
        initial = super(add_comment, self).get_initial(**kwargs)
        initial['user'] = self.request.user
        print(self.kwargs['pk'])
        sub_task = get_object_or_404(SubTask, pk=self.kwargs['pk'])
        initial['Subtask'] = sub_task
        return initial

    def clean_email(self):
        data = self.self.cleaned_data.get('user')
        print('data')
        if data is not self.request.user:
            raise ValidationError("You have forgotten about Fred!")
        return data

    def clean_user(self):
        user = self.cleaned_data['user']
        print(user)
        if user is not self.request.user:
            raise forms.ValidationError("You have to use your name.")
        return user

    def form_valid(self, form):
        u = str(form.cleaned_data['user'])
        user = str(self.request.user)
        print(user)
        s_t = form.cleaned_data['Subtask']
        sub_task = get_object_or_404(SubTask, pk=self.kwargs['pk'])
        uu = str(user)
        print(uu)
        if u != user:
            raise forms.ValidationError("You have to use your name.")
        if s_t != sub_task:
            raise forms.ValidationError("You have to choose." + sub_task.__str__())
        return super().form_valid(form)


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

    #
    # def get_form(self, form_class):
    #     form = super(TaskCreate, self).get_form(form_class)
    #     form.fields['project'].queryset = Project.objects.filter(
    #                                            type=self.request.GET['type'])
    #     return form

    # def get_context_data(self, **kwargs):
    #     context = super(add_comment, self).get_context_data(**kwargs)
    #     context['task_id'] = self.kwargs['t']
    #     return context
    #
    # def get_initial(self, *args, **kwargs):
    #     initial = super(add_comment, self).get_initial(**kwargs)
    #     initial['Subtask'] = self.kwargs['t']
    #     return initial
