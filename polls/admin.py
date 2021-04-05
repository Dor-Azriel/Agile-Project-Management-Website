from django.contrib import admin

from .models import Question
class YourModel(admin.ModelAdmin):
    pass
admin.site.register(Question,YourModel)
