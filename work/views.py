from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import DateInput
from django.shortcuts import render, redirect, get_object_or_404

from Message.models import Messages
from .forms import SubTaskForm
from django import forms
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Comment, Sprint, project, SubTask, Sprint_Task
from .models import Task


# startTime = forms.DateField(widget=forms.SelectDateWidget)

class add_subtask(CreateView, LoginRequiredMixin, ):
    model = SubTask
    fields = ['TaskName','startTime', 'endTime', 'encharge', 'lastUpdate', 'cost', 'workDone', 'skillNeed', ]

    def get_form_kwargs(self):
        kwargs = super(add_subtask, self).get_form_kwargs()
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        if kwargs['instance'] is None:
            kwargs['instance'] = SubTask()
        kwargs['instance'].TaskID = task
        kwargs['instance'].Description = str(task.id) + " - " +task.TaskName
        print(kwargs)
        return kwargs


class update_subtask(UpdateView, LoginRequiredMixin, ):
    model = SubTask
    fields = ['TaskName','startTime', 'endTime', 'encharge', 'lastUpdate', 'cost', 'workDone', 'skillNeed', ]


class subtask_delete(DeleteView):
    model = SubTask

    def get_success_url(self):
        return reverse_lazy('manager_task_view', kwargs={'task_id': self.kwargs['task_id']})


class add_comment(CreateView, LoginRequiredMixin, ):
    model = Comment
    fields = ['body']

    def get_form_kwargs(self):
        kwargs = super(add_comment, self).get_form_kwargs()
        sub_task = get_object_or_404(SubTask, pk=self.kwargs['pk'])
        if kwargs['instance'] is None:
            kwargs['instance'] = Comment()
        kwargs['instance'].user = self.request.user
        kwargs['instance'].Subtask = sub_task
        # print(kwargs)
        print('sdfsdfsdff')
        return kwargs


class update_comment(UpdateView, LoginRequiredMixin):
    model = Comment
    fields = ['body']


class delete_comment(DeleteView, LoginRequiredMixin):
    model = Comment
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('manager_subtask_view', kwargs={'sub_task_id': self.kwargs['subtask_id']})


class add_task(CreateView, ):
    model = Task
    fields = ['TaskName','startTime', 'endTime', 'inCharge', 'workDone', 'lastUpdate', 'cost', 'Description' ]

    def get_form_kwargs(self):
        kwargs = super(add_task, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Task()
        kwargs['instance'].projectnum = get_object_or_404(project, pk=self.kwargs['pk'])
        print(kwargs)
        return kwargs


class update_task(UpdateView, LoginRequiredMixin):
    model = Task
    fields = ['TaskName','startTime', 'endTime', 'inCharge', 'workDone', 'lastUpdate', 'cost', 'Description',
              ]


class task_delete(DeleteView):
    model = Task

    def get_success_url(self):

        print(self.kwargs['route'])
        if self.kwargs['route'] == 'sprint':
            print('delete check')
            return reverse_lazy('manager_views_sprints', kwargs={'sprint_id': self.kwargs['r_id']})
        else:
            return reverse_lazy('manager_views_projects', kwargs={'project_id': self.kwargs['r_id']})


class add_sprint(CreateView, LoginRequiredMixin):
    model = Sprint
    fields = ['SprintName', 'StartTime', 'endTime', 'cost', 'Descripion']

    def get_form_kwargs(self):
        kwargs = super(add_sprint, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Sprint()
        kwargs['instance'].projectnum = get_object_or_404(project, pk=self.kwargs['pk'])
        print(kwargs)
        return kwargs

    # def form_valid(self, form):
    #     p = form.cleaned_data['projectnum']
    #     proj = get_object_or_404(project, pk=self.kwargs['pk'])
    #     if p != proj:
    #         raise forms.ValidationError("You have to choose." + proj.__str__())
    #     return super().form_valid(form)
    #
    # def get_initial(self, *args, **kwargs):
    #     initial = super(add_sprint, self).get_initial(**kwargs)
    #     p = get_object_or_404(project, pk=self.kwargs['pk'])
    #     initial['projectnum'] = p
    #     return initial


class update_sprint(UpdateView, LoginRequiredMixin):
    model = Sprint
    fields = ['SprintName', 'StartTime', 'endTime', 'cost', 'Descripion']


class delete_sprint(DeleteView):
    model = Sprint

    def get_success_url(self):
        return reverse_lazy('manager_views_projects', kwargs={'project_id': self.kwargs['project_id']})


def send_message(request, project_id):
    print(project_id)
    p = get_object_or_404(project, id=project_id)
    m = Messages(sender=str(request.user.username), reciver=p.manager,
                 message="Contact  " + request.user.username.__str__() + ' about ' + p.__str__(), Subject='Alert')
    m.save()
    return redirect('ClientHome_views')


class add_project(CreateView, LoginRequiredMixin):
    model = project
    fields = ['ProjectName', 'endTime', 'client',
              'Budget', 'currentBudgeSchedule', 'MoneySpends', 'Description']

    def get_form_kwargs(self):
        kwargs = super(add_project, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = project()
        kwargs['instance'].manager = self.request.user
        print(kwargs)
        return kwargs


class update_project(UpdateView, LoginRequiredMixin):
    model = project
    fields = ['ProjectName', 'endTime', 'client',
              'Budget', 'currentBudgeSchedule', 'MoneySpends', 'Description']


class delete_project(DeleteView, LoginRequiredMixin):
    model = project
    fields = '__all__'

    def get_success_url(self):
        return reverse('manager', kwargs={})


class InputForm(forms.Form):
    work_done = forms.IntegerField(max_value=100, min_value=0)


class add_sprint_task(CreateView, ):
    model = Sprint_Task
    fields = ['TaskId']

    def get_form_kwargs(self):
        kwargs = super(add_sprint_task, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Sprint_Task()
        kwargs['instance'].SpirntId = get_object_or_404(Sprint, pk=self.kwargs['sprint'])
        print(kwargs)
        return kwargs

    def form_valid(self, form):
        sprint = get_object_or_404(Sprint, pk=self.kwargs['sprint'])
        tasks = Task.objects.all().filter(projectnum=self.kwargs['p'], inSprint=True)
        t = form.cleaned_data['TaskId']
        if t in tasks:
            raise forms.ValidationError("This task already in sprint.")
        if t not in tasks:
            print('inser to sprint')
            t.inserted_to_sprint()
            print(t.inSprint)
        return super().form_valid(form)

    def get_initial(self, *args, **kwargs):
        initial = super(add_sprint_task, self).get_initial(**kwargs)
        print(self.kwargs['sprint'])
        s = get_object_or_404(Sprint, pk=self.kwargs['sprint'])
        print(s)
        initial['SpirntId'] = s
        return initial


class delete_sprint_task(DeleteView, ):
    model = Sprint_Task
    fields = '__all__'


    def get_success_url(self):
        print('aaaaaaaaaaaa')
        return reverse_lazy('manager_views_sprints', kwargs={'sprint_id': self.kwargs['sprint'],
                    'tid':self.kwargs['taskid'], 'need_to_delete': 1})


def work_done_sub(request, my_id):
    sub_task = get_object_or_404(SubTask, id=my_id)
    sub_task.workIsDone()
    return redirect('SubTaskComment_view', my_id)


def read_bool(request, my_id):
    print('my_id')
    m = get_object_or_404(Messages, id=my_id)
    m.isRead()
    return redirect('MessagePage_view')
