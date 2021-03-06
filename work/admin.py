from django.contrib import admin
from .models import skill
from .models import SubTask
from .models import Task
from .models import project
from .models import Sprint
from .models import review
from .models import Conclusions,Sprint_Task

class SubTaskInline(admin.TabularInline):
    model=SubTask

class TaskAdmin(admin.ModelAdmin):
        inlines =[ SubTaskInline,]

# class TaskInline(admin.TabularInline):
#     model=Task
#
# class SprintAdmin(admin.ModelAdmin):
#         inlines =[ TaskInline,]

class SprintInline(admin.TabularInline):
    model = Sprint


class ProjectAdmin(admin.ModelAdmin):
    inlines = [SprintInline, ]

admin.site.register(skill)
admin.site.register(SubTask)
admin.site.register(Task,TaskAdmin)
admin.site.register(Sprint)
admin.site.register(project,ProjectAdmin)
admin.site.register(review)
admin.site.register(Conclusions),
admin.site.register(Sprint_Task)