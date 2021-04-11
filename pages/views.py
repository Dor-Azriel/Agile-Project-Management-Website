from django.core.mail.backends import console
from django.shortcuts import render
from work.models import Task
from django.shortcuts import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {});


def task_views(request, *args, **kwargs):
    obj = Task.objects.order_by()
    return render(request, "task.html", {'tasks': obj, })


def task_sorted_by_date(request, *args, **kwargs):
    obj = Task.objects.all()
    obj = map(lambda x, y: min(x.startTime, y.startTime), obj )

    return render(request, "task.html", {'tasks': obj, })


