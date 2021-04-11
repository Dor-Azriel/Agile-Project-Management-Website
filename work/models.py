from django.core.validators import  MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class skill(models.Model):
    languages=[(1,'Java'),(2,'C'),(3,'C++'),(4,'Python'),(5,'C#'),(6,'React'),(7,'HTML'),(8,'php'),(9,'DB')]
    language=models.CharField(max_length=100,choices=languages)
    levels = [(1,'Junior'),(2,'Senior'),(3,'expert')]
    level=models.CharField(max_length=6,choices=levels,default=levels[0])
    def __str__(self):
        return self.language+self.level

class SubTask(models.Model):
    startTime =models.DateField(null=False)
    endTime = models.DateField(null=False)
    encharge =models.ForeignKey(User,on_delete=models.CASCADE)
    lastUpdate = models.DateTimeField(null=True)
    cost = models.FloatField(null=False,)
    skillNeed= models.ForeignKey(skill,on_delete=models.CASCADE)
    TaskName = models.CharField(max_length=300, null=False)
    Description = models.CharField(max_length=500, null=True)


class Task(models.Model):
    startTime =models.DateField(null=False)
    endTime = models.DateField(null=False)
    inCharge =models.ForeignKey(User,on_delete=models.CASCADE)
    workDone =models.IntegerField(default=1,validators=[MaxValueValidator(100),MinValueValidator(1)])
    lastUpdate = models.DateTimeField(null=False)
    cost = models.FloatField(null=False,)
    subTasks = models.ForeignKey(SubTask,on_delete=models.CASCADE)
    TaskName = models.CharField(max_length=300,null=False)
    Description = models.CharField(max_length=500,null=True)

class project(models.Model):
    ProjectName = models.CharField(max_length=300, null=False)
    Description = models.CharField(max_length=500, null=True)
    startTime = models.DateField(null=False)
    endTime = models.DateField(null=False)
    allTasks = models.ForeignKey(Task, on_delete=models.CASCADE)