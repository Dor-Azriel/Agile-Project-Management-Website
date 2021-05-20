from django.core.mail.backends import console
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from work.forms import CommentForm
from work.models import Task
from django.shortcuts import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    obj = Task.objects.order_by()
    return render(request, "base.html", {'tasks': obj, });


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
            comment.task = task
            comment.save()
            return render(request, "oneTask.html", {'t': task})
            # return task.get_absoulte_url
    else:
        CommentForm()
    return render(request, "addComment.html", {'t': task})