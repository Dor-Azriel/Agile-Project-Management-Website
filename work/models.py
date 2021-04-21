from django.core.validators import  MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class skill(models.Model):
    languages=[('JA','Java'),('CC','C'),('C+','C++'),('PY','Python'),('C#','C#'),('RE','React'),('HT','HTML'),('PH','php'),('DB','DB')]
    language=models.CharField(max_length=2,default='JA',choices=languages,)
    levels = [('JU','Junior'),('SE','Senior'),('EX','expert')]
    level=models.CharField(max_length=2,choices=levels,default='JU',)
    def __str__(self):
        return self.language+self.level
    def is_upperclass(self):
        return self.language+self.level

class SubTask(models.Model):
    startTime =models.DateField(null=False)
    endTime = models.DateField(null=False)
    encharge =models.ForeignKey(User,on_delete=models.CASCADE)
    lastUpdate = models.DateTimeField(null=True)
    cost = models.FloatField(null=False,default=0)
    workDone = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
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

class Sprint(models.Model):
    SprintName = models.CharField(max_length=300,null=False)
    Descripion = models.CharField(max_length=300,null=False)
    StartTime = models.DateTimeField(null=False)
    endTime = models.DateTimeField(null=False)
    allTasks = models.ForeignKey(Task, on_delete=models.CASCADE)

class project(models.Model):
    ProjectName = models.CharField(max_length=300, null=False)
    Description = models.CharField(max_length=500, null=True)
    startTime = models.DateField(null=False)
    endTime = models.DateField(null=False)
    allSprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)

class review(models.Model):
    ProjectName = models.CharField(max_length=300, null=False)
    Description = models.CharField(max_length=500, null=True)
    TaskReview = models.ForeignKey(Task, on_delete=models.CASCADE)