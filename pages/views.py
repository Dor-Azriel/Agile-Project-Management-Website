from django.core.mail.backends import console
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate,login
from work.forms import CommentForm
from work.models import Task,project,Sprint,SubTask,Comment
from django.shortcuts import HttpResponse
from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from Message.models import Messages

# Create your views here.
def home_view(request, *args, **kwargs):
    obj = Task.objects.order_by()
    return render(request, "base.html", {'tasks': obj, });

def logd_view(request):
    username = request.user.groups.all()
    lists= request.user.is_superuser
    if (lists==True):
        return HttpResponseRedirect(reverse('admin:index'))
    elif username[0].name == 'client':
        obj = Task.objects.all();
        return render(request, "DevlopHome.html",{'tasks': obj})
    elif username[0].name == 'Developer':
        return redirect('DevlopHome_views')

def MessagePage_view(request):
    list = Messages.objects.all().filter(reciver=request.user.id,readConf=False)
    return render(request, "MessagesPage.html", {'tasks': list})

def manager_views(request):
    filt=request.user.id;
    obj = project.objects.all().filter(manager=filt);
    obj2={'name':request.user.username}
    return render(request, "manager_home.html", {'tasks': obj,'name':obj2})


def DevlopHome_views(request):
    filt=request.user.id;
    obj = project.objects.all().filter(inCharge=filt);
    obj2={'name':request.user.username}
    return render(request, "DevlopHome.html", {'projects': obj,'name':obj2})

def ClientHome_views(request):
    pro= project.objects.all().filter(client=request.user.id)
    # for proj in pro :
    #     tasks =
def SubTasksPerTask_view(request,id):
    obj= SubTask.objects.filter(TaskID=id)
    obj2=Task.objects.filter(id=id)
    return render(request, "SubTasksPerTask.html", {'tasks': obj,'t': obj2, })

def SubTaskComment_view(request,id,my_id):
    obj= SubTask.objects.filter(id=my_id)
    obj2=Comment.objects.filter(Subtask=my_id)
    return render(request, "SubTaskComment.html", {'tasks': obj,'t': obj2, })


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


# def add_C(request, id):
#     task = get_object_or_404(Task, id=id)
#     if request == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.task = task
#             # return task.get_absoulte_url
#     else:
#         CommentForm()
#     return render(RequestContext(request), "addComment.html", {'t': task})


def add_comment(request, id):
    task = get_object_or_404(Task, id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return render(request, "oneTask.html", {'t': task})
            # return task.get_absoulte_url
    else:
        CommentForm()
    return render(request, "addComment.html", {'t': task})