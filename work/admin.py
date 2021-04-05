from django.contrib import admin
from .models import skill
from .models import SubTask
from .models import Task

admin.site.register(skill)
admin.site.register(SubTask)
admin.site.register(Task)
