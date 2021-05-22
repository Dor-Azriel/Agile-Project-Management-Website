from django.shortcuts import render, redirect
from .forms import SubTaskForm
from django import forms

def create_sub_task(request):
    print('sdfdf')
    name = request.user.username
    form = SubTaskForm()
    print(name)
    if request.method == 'POST':
        form = SubTaskForm(request.POST)
        if form.is_valid():
            # print(form)
            form.save()
            print('eshhhh')
        else:
            print(form.errors)

    dict = {'form': form, }
    return render(request, "subTask.html", dict)




