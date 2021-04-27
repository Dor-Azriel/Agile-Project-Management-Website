from django.contrib import admin
from .models import skill
from .models import SubTask
from .models import Task
from .models import project
from .models import Sprint
from .models import review
from .models import Conclusions

admin.site.register(skill)
admin.site.register(SubTask)
admin.site.register(Task)
admin.site.register(Sprint)
admin.site.register(project)
admin.site.register(review)
admin.site.register(Conclusions)