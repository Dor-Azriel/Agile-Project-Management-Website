from django import forms
from django.forms import DateInput
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .models import Comment
from .models import SubTask
from .models import Task


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'email', 'body')


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        SubTask.startTime = forms.DateField(widget=DateInput)
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
