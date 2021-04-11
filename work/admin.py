from django.contrib import admin
from .models import skill
from .models import SubTask
from .models import Task
from .models import project

admin.site.register(skill)
admin.site.register(SubTask)
admin.site.register(Task)
admin.site.register(project)