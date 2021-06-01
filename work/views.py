from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.forms import DateInput
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SubTaskForm
from django import forms
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Comment, Sprint, project, SubTask, Sprint_Task
from .models import Task


# startTime = forms.DateField(widget=forms.SelectDateWidget)

class add_subtask(CreateView, LoginRequiredMixin, ):
    model = SubTask
    fields = '__all__'

    def get_initial(self, *args, **kwargs):
        initial = super(add_subtask, self).get_initial(**kwargs)
        # print(self.kwargs['pk'])
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        initial['TaskName'] = task.TaskName
        initial['TaskID'] = task.id
        return initial

    def form_valid(self, form):
        t_n = form.cleaned_data['TaskName']
        t_id = form.cleaned_data['TaskID']
        task = get_object_or_404(Task, pk=self.kwargs['pk'])

        if t_n != task.TaskName:
            raise forms.ValidationError("You have to choose " + str(task.TaskName))
        if t_id.id != task.id:
            raise forms.ValidationError("You have to choose." + str(task.id))
        return super().form_valid(form)


class update_subtask(UpdateView, LoginRequiredMixin, ):
    model = SubTask
    fields = '__all__'

    def form_valid(self, form):
        t_n = form.cleaned_data['TaskName']
        t_id = form.cleaned_data['TaskID']
        task = get_object_or_404(Task, pk=self.kwargs['pk'])

        if t_n != task.TaskName:
            raise forms.ValidationError("You have to choose " + str(task.TaskName))
        if t_id.id != task.id:
            raise forms.ValidationError("You have to choose." + str(task.id))
        return super().form_valid(form)


class subtask_delete(DeleteView):
    model = SubTask

    def get_success_url(self):
        return reverse_lazy('manager_task_view', kwargs={'task_id': self.kwargs['task_id']})


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


class add_task(CreateView, ):
    model = Task
    fields = '__all__'

    def form_valid(self, form):
        p = form.cleaned_data['projectnum']
        proj = get_object_or_404(project, pk=self.kwargs['pk'])
        if p != proj:
            raise forms.ValidationError("You have to choose." + proj.__str__())
        return super().form_valid(form)

    def get_initial(self, *args, **kwargs):
        initial = super(add_task, self).get_initial(**kwargs)
        print('gvfff')
        p = get_object_or_404(project, pk=self.kwargs['pk'])
        initial['projectnum'] = p
        return initial


class update_task(UpdateView, LoginRequiredMixin):
    model = Task
    fields = '__all__'

    def form_valid(self, form):
        p = form.cleaned_data['projectnum']
        proj = get_object_or_404(project, pk=self.kwargs['pk'])
        if p != proj:
            raise forms.ValidationError("You have to choose." + proj.__str__())
        return super().form_valid(form)


class add_sprint(CreateView, LoginRequiredMixin):
    model = Sprint
    fields = '__all__'


class update_sprint(UpdateView, LoginRequiredMixin):
    model = Sprint
    fields = '__all__'


class add_project(CreateView, LoginRequiredMixin):
    model = project
    fields = '__all__'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class update_project(UpdateView, LoginRequiredMixin):
    model = project
    fields = '__all__'


class InputForm(forms.Form):
    work_done = forms.IntegerField(max_value=100, min_value=0)


class add_sprint_task(CreateView, ):
    model = Sprint_Task
    fields = '__all__'

    def form_valid(self, form):
        s = form.cleaned_data['SpirntId']
        sprint = get_object_or_404(Sprint, pk=self.kwargs['sprint'])
        tasks = Task.objects.all().filter(projectnum=self.kwargs['p'])
        tasks = tasks.filter(inSprint=True)
        t = form.cleaned_data['TaskId']
        if t in tasks:
            raise forms.ValidationError("This task already in sprint.")
        if s != sprint:
            raise forms.ValidationError("You have to choose." + sprint.__str__())
        if t not in tasks and s == sprint:
            t.inserted_to_sprint
        return super().form_valid(form)

    def get_initial(self, *args, **kwargs):
        initial = super(add_sprint_task, self).get_initial(**kwargs)
        print(self.kwargs['sprint'])
        s = get_object_or_404(Sprint, pk=self.kwargs['sprint'])
        print(s)
        initial['SpirntId'] = s
        return initial
