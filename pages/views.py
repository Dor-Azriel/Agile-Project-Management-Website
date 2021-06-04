from django.core.mail.backends import console
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from work.models import Task, project, Sprint, SubTask, Comment, Sprint_Project, Sprint_Task
from django.shortcuts import HttpResponse
from django.contrib import admin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from Message.models import Messages
from django.db import models

# Create your views here.
from work.views import InputForm, add_project


def home_view(request, *args, **kwargs):
    username = request.user.groups.all()
    if request.user.groups.all():
        if username[0].name == 'client':
            return redirect('ClientHome_views')
        elif username[0].name == 'Developer':
            return redirect('DevlopHome_views')
        elif username[0].name == 'projectManager':
            return redirect('manager')
    return render(request, "StartPage.html", )


def logout_view(request):
    logout(request)
    return render(request, "StartPage.html", )


def logd_view(request):
    username = request.user.groups.all()
    lists = request.user.is_superuser
    if (lists == True):
        return HttpResponseRedirect(reverse('admin:index'))
    elif username[0].name == 'client':
        return redirect('ClientHome_views')
    elif username[0].name == 'Developer':
        return redirect('DevlopHome_views')
    elif username[0].name == 'projectManager':
        return redirect('manager')


def ClientSprint_view(request, id):
    spri = Sprint.objects.all().filter(projectnum=id)
    tasks = Task.objects.all().filter(projectnum=id, inSprint=False)
    for s in spri:
        s.taskDone = 0
        j = 0
        if Sprint_Task.objects.all().filter(SpirntId=s.id):
            ts = Sprint_Task.objects.all().filter(SpirntId=s.id)
            for t in ts:
                if Task.objects.all().filter(id=t.id, workDone=100):
                    j += 1
            s.taskDone = j / Sprint_Task.objects.all().filter(SpirntId=s.id).count() * 100

    return render(request, "ClientSprint.html", {'sprints': spri, 'tasks': tasks})


def MessagePage_view(request):
    list = Messages.objects.all().filter(reciver=request.user.id, readConf=False).order_by("date")
    return render(request, "MessagesPage.html", {'tasks': list})


def manager_views(request):
    filt = request.user.id;
    obj = project.objects.all().filter(manager=filt);
    obj2 = {'name': request.user.username}
    for p in obj:
        if p.currentBudgeSchedule and p.Budget:
            p.stat = p.currentBudgeSchedule / p.Budget * 100
    msgcount = Messages.objects.all().filter(reciver=request.user.id, readConf=False).count()
    return render(request, "manager_home.html", {'projects': obj, 'name': obj2, 'msgcount': msgcount})


def manager_views_projects(request, project_id):
    tasks = Task.objects.all().filter(projectnum=project_id, inSprint=False)
    sprints = Sprint.objects.all().filter(projectnum=project_id)
    p = get_object_or_404(project, id=project_id)
    p.count = 0
    if Task.objects.all().filter(projectnum=project_id, workDone=100):
        p.count = Task.objects.all().filter(projectnum=project_id, workDone=100).count() / Task.objects.all().filter(
            projectnum=project_id).count() * 100
    route = 'project'
    return render(request, "manager_project_view.html", {'tasks': tasks, 'sprints': sprints, 'p': p, 'route': route})


def manager_views_sprints(request, sprint_id, need_to_delete = False,tid = None):
    if need_to_delete:
        t = get_object_or_404(Task, id=tid)
        t.removeFromSprint()
    tasks = Sprint_Task.objects.all().filter(SpirntId=sprint_id)
    sprint = get_object_or_404(Sprint, id=sprint_id)
    p = sprint.projectnum
    route = 'sprint'
    print(route)
    return render(request, "manager_sprint_view.html",
                  {'tasks': tasks, 'sprint': sprint, 'p': p.pk, 'route': route})



def manager_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    # print('maegiaa?')
    if task.inSprint:
        print('inside sprint')
        route = 'sprint'
        t = get_object_or_404(Sprint_Task, TaskId=task)
        r_id = t.SpirntId.id
    else:
        route = 'project'
        r_id = task.projectnum.id
    sub_tasks = SubTask.objects.filter(TaskID=task)
    print(task)

    return render(request, "manager_task_view.html",
                  {'task': task, 'sub_tasks': sub_tasks, 'r_id': r_id, 'route': route})


def manager_subtask_view(request, sub_task_id):
    sub_task = get_object_or_404(SubTask, id=sub_task_id)
    task = sub_task.TaskID
    comments = Comment.objects.filter(Subtask=sub_task_id)
    print(comments)
    msgcount = Messages.objects.all().filter(reciver=request.user.id, readConf=False).count()
    return render(request, "manager_subtask_view.html",
                  {'sub_task': sub_task, 'comments': comments, 'task': task, 'msgcount': msgcount})


def SubTaskComment_view(request, my_id):
    obj = get_object_or_404(SubTask, id=my_id)
    obj2 = Comment.objects.filter(Subtask=my_id)
    print(obj.pk)
    if request.user.groups.all()[0].name == "Developer":
        msgcount = Messages.objects.all().filter(reciver=request.user.id, readConf=False).count()
        return render(request, "SubTaskComment.html", {'task': obj, 'comments': obj2, 'msgcount': msgcount})
    return redirect('manager_subtask_view', my_id)


def DevlopHome_views(request):
    filt = request.user.id
    obj = Task.objects.all().filter(inCharge=filt);
    obj2 = {'name': request.user.username}
    msgcount = Messages.objects.all().filter(reciver=request.user.id, readConf=False).count()
    return render(request, "DevlopHome.html", {'tasks': obj, 'name': obj2, 'msgcount': msgcount})


def ClientHome_views(request):
    pro = project.objects.all().filter(client=request.user)
    for p in pro:
        p.Scheduled = p.currentBudgeSchedule / p.Budget * 100
        p.Balance = p.MoneySpends / p.Budget * 100
        if Task.objects.all().filter(projectnum=p.id, workDone=100).count() and Task.objects.all().filter(
                projectnum=p.id).count():
            p.taskDone = Task.objects.all().filter(projectnum=p.id, workDone=100).count() / Task.objects.all().filter(
                projectnum=p.id).count() * 100
        else:
            p.taskDone = 0
    obj2 = {'name': request.user.username}
    msgcount = Messages.objects.all().filter(reciver=request.user.id, readConf=False).count()
    return render(request, "ClientHome.html", {'projects': pro, 'name': obj2, 'msgcount': msgcount})


def ClientSprint_view(request, id):
    tasks = Task.objects.all().filter(projectnum=id, inSprint=False)
    sprints = Sprint.objects.all().filter(projectnum=id)
    for s in sprints:
        s.count = 0
        tmp = Sprint_Task.objects.all().filter(SpirntId=s.id)
        for t in tmp:
            if t.TaskId.workDone == 100:
                s.count += 1
        s.count = s.count / Sprint_Task.objects.all().filter(SpirntId=s.id).count() * 100
    msgcount = Messages.objects.all().filter(reciver=request.user.id, readConf=False).count()
    return render(request, "ClientSprint.html", {'tasks': tasks, 'sprints': sprints, 'msgcount': msgcount})


def Client_Task_per_Sprint(request, id, sprint_id):
    tasks = Sprint_Task.objects.all().filter(SpirntId=sprint_id)
    sprint = get_object_or_404(Sprint, id=sprint_id)
    sprint.count = 0
    sprint.budg = 0
    tmp = Sprint_Task.objects.all().filter(SpirntId=sprint.id)
    for t in tmp:
        if t.TaskId.workDone == 100:
            sprint.count += 1
            sprint.budg += t.TaskId.cost
    sprint.count = sprint.count / Sprint_Task.objects.all().filter(SpirntId=sprint.id).count() * 100
    if sprint.cost:
        sprint.budg = sprint.budg / sprint.cost * 100
        msgcount = Messages.objects.all().filter(reciver=request.user.id, readConf=False).count()
    return render(request, "Client_Task_per_sprint.html",
                  {'tasks': tasks, 'sprint': sprint, 'msgcount': msgcount})


def SubTasksPerTask_view(request, id):
    obj = SubTask.objects.filter(TaskID=id)
    obj2 = Task.objects.filter(id=id)
    msgcount = Messages.objects.all().filter(reciver=request.user.id, readConf=False).count()
    return render(request, "SubTasksPerTask.html", {'tasks': obj, 't': obj2, 'msgcount': msgcount})


def task_views(request, *args, **kwargs):
    obj = Task.objects.order_by()
    return render(request, "task.html", {'tasks': obj, })


def task_sorted_by_date(request, *args, **kwargs):
    obj = Task.objects.all().order_by("startTime");
    return render(request, "task.html", {'tasks': obj})


def task_sorted_by_done(request, *args, **kwargs):
    obj = Task.objects.all().order_by("workDone");
    return render(request, "task.html", {'tasks': obj})


def task_detail(request, slug):
    task = get_object_or_404(Task)
    return render(request, "oneTask.html", {'task': task})


def dynamic_view(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, "oneTask.html", {'t': task})


def work_done(request, id):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            print(id)
            task = get_object_or_404(Task, id=id)
            print(form.cleaned_data['work_done'])
            task.workDone = form.cleaned_data['work_done']
            task.save()
    filt = request.user.id
    f = InputForm()
    obj = Task.objects.all().filter(inCharge=filt);
    obj2 = {'name': request.user.username}
    return render(request, "DevlopHome.html", {'tasks': obj, 'name': obj2, 'form': f})
