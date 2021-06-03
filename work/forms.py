from django import forms
from django.forms import DateInput
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .models import Comment
from .models import SubTask
from .models import Task





class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        SubTask.startTime = forms.DateField(widget=DateInput)
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
