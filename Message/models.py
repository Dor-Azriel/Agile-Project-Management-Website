from django.db import models
from django.contrib.auth.models import User
from work.models import Task,SubTask,project,Sprint
from django.db.models.signals import post_save,pre_save
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render
from datetime import timedelta
from datetime import datetime
import pytz

# Create your models here.

class Messages(models.Model):
    sender = models.CharField(max_length=300, null=False)
    reciver = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    message= models.CharField(max_length=500, null=False)
    date = models.DateField(auto_now_add=True,null=False)
    Subject= models.CharField(max_length=300, null=False)
    readConf= models.BooleanField(default=False)

    def isRead(self):
        self.readConf = True
        self.save()


def Send_Conected(sender,user,request,**kwargs):
        groups= user.groups.all()
        if groups:
            if groups[0].name=='Developer':
                tasks= Task.objects.all().filter(inCharge=user.id)
                for task in tasks:
                    #task.lastUpdate = task.lastUpdate.replace(tzinfo=pytz.UTC)
                    #and  datetime.date(datetime.now())-task.lastUpdate > timedelta(days=1)
                    if task.endTime - datetime.date(datetime.now()) == timedelta(days=2)  :
                        msg=Messages.objects.create(message="Two days left to complete task - "+task.TaskName,reciver=user,sender="System Message",
                                                   Subject="Reminder")
                        msg.save()
                        task.lastUpdate=datetime.date(datetime.now())

                return render(request, "DevlopHome.html")

            if groups[0].name == 'client':
                projects= project.objects.all().filter(client=user.id)
                for pro in projects:
                    if pro.Budget-pro.MoneySpends <= 0:
                        msg = Messages.objects.create(message="Project " + pro.ProjectName + ", out of Budget.",
                                                     reciver=user, sender="System Message",
                                                     Subject="Alert")
                        msg.save()
                    if pro.Budget-pro.currentBudgeSchedule < pro.Budget*0.25:
                        msg = Messages.objects.create(message="Project " + pro.ProjectName + " have 25% Budget left as scheduled.",
                                                     reciver=user, sender="System Message",
                                                     Subject="Alert")
                        msg.save()
                return render(request, "ClientHome.html")
        return render(request, "DevlopHome.html")



user_logged_in.connect(Send_Conected)