from django.contrib import admin

from .models import Question
from .models import Chat

class YourModel(admin.ModelAdmin):
    pass
admin.site.register(Question,YourModel)


admin.site.register(Chat,YourModel)
