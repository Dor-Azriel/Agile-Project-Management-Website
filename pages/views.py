from django.core.mail.backends import console
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from work.forms import CommentForm
from work.models import Task, project, Sprint, SubTask, Comment, Sprint_Project, Sprint_Task
from django.shortcuts import HttpResponse
from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from Message.models import Messages

# Create your views here.
from work.views import InputForm, add_project


def home_view(request, *args, **kwargs):
    obj = Task.objects.order_by()
    return render(request, "base.html", {'tasks': obj, });


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


def MessagePage_view(request):
    list = Messages.objects.all().filter(reciver=request.user.id, readConf=False)
    return render(request, "MessagesPage.html", {'tasks': list})


def manager_views(request):
    filt = request.user.id;
    obj = project.objects.all().filter(manager=filt);
    obj2 = {'name': request.user.username}
    return render(request, "manager_home.html", {'projects': obj, 'name': obj2})


def manager_views_projects(request, project_id):
    tasks = Task.objects.all().filter(projectnum=project_id)
    sprints = Sprint.objects.all().filter(projectnum=project_id)
    p = get_object_or_404(project, id=project_id)
    return render(request, "manager_project_view.html", {'tasks': tasks, 'sprints': sprints, 'p': p})


def manager_views_sprints(request, sprint_id):
    tasks = Sprint_Task.objects.all().filter(SpirntId=sprint_id)
    print(tasks[0].TaskId)
    sprint = get_object_or_404(Sprint, id=sprint_id)
    p = sprint.projectnum
    print(p)
    return render(request, "manager_sprint_view.html",
                  {'tasks': tasks, 'sprint': sprint, 'p': p.pk})


def DevlopHome_views(request):
    filt = request.user.id;
    obj = Task.objects.all().filter(inCharge=filt);
    obj2 = {'name': request.user.username}
    return render(request, "DevlopHome.html", {'tasks': obj, 'name': obj2})


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
    return render(request, "ClientHome.html", {'projects': pro, 'name': obj2})


def ClientSprint_view(request, id):
    spri = Sprint_Project.objects.all().filter(ProjectId=id)
    return render(request, "ClientSprint.html", {'sprints': spri, })


def SubTasksPerTask_view(request, id):
    obj = SubTask.objects.filter(TaskID=id)
    obj2 = Task.objects.filter(id=id)
    return render(request, "SubTasksPerTask.html", {'tasks': obj, 't': obj2, })


def SubTaskComment_view(request, id, my_id):
    obj = get_object_or_404(Task, id=id)
    obj2 = Comment.objects.filter(Subtask=my_id)
    print(obj.pk)
    return render(request, "SubTaskComment.html", {'task': obj, 'comments': obj2, })


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
