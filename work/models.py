from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save, pre_save


# Create your models here.

# class categories(models.Model):
#     status = ['Done','In Progress','Not released']


class skill(models.Model):
    languages = [('JA', 'Java'), ('CC', 'C'), ('C+', 'C++'), ('PY', 'Python'), ('C#', 'C#'), ('RE', 'React'),
                 ('HT', 'HTML'), ('PH', 'php'), ('DB', 'DB')]
    language = models.CharField(max_length=2, default='JA', choices=languages, )
    levels = [('JU', 'Junior'), ('SE', 'Senior'), ('EX', 'expert')]
    level = models.CharField(max_length=2, choices=levels, default='JU', )

    def __str__(self):
        return self.language + self.level

    def is_upperclass(self):
        return self.language + self.level


class project(models.Model):
    ProjectName = models.CharField(max_length=300, null=False)
    Description = models.CharField(max_length=500, null=True)
    startTime = models.DateField(null=False, auto_now=True)
    endTime = models.DateField(null=False)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, related_name="project_manager", on_delete=models.CASCADE)
    Budget = models.FloatField(null=False, default=0)
    currentBudgeSchedule = models.FloatField(null=False, default=0)
    MoneySpends = models.FloatField(null=False, default=0)

    def get_absolute_url(self):
        return reverse('manager', kwargs={})


class Sprint(models.Model):
    SprintName = models.CharField(max_length=300, null=False)
    Descripion = models.CharField(max_length=300, null=False)
    StartTime = models.DateTimeField(null=False)
    endTime = models.DateTimeField(null=False)
    projectnum = models.ForeignKey(project, on_delete=models.CASCADE)
    cost = models.FloatField(null=False, default=0)

    def get_absolute_url(self):
        return reverse('manager_views_projects', kwargs={'project_id': self.projectnum.id})


class Task(models.Model):
    startTime = models.DateField(null=False)
    endTime = models.DateField(null=False)
    inCharge = models.ForeignKey(User, on_delete=models.CASCADE)
    workDone = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    lastUpdate = models.DateTimeField(null=False)
    cost = models.FloatField(null=False, default=0)
    TaskName = models.CharField(max_length=300, null=False)
    Description = models.CharField(max_length=500, null=True)
    projectnum = models.ForeignKey(project, on_delete=models.CASCADE)
    inSprint = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('manager_views_projects', kwargs={'project_id': self.projectnum.id})

    def inserted_to_sprint(self):
        self.inSprint = True
        self.save()


class Sprint_Project(models.Model):
    ProjectId = models.ForeignKey(project, on_delete=models.CASCADE)
    SprintId = models.ForeignKey(Sprint, on_delete=models.CASCADE)


class Sprint_Task(models.Model):
    SpirntId = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    TaskId = models.ForeignKey(Task, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('manager_views_sprints', kwargs={'sprint_id': self.SpirntId.id})


class SubTask(models.Model):
    startTime = models.DateField(null=False)
    endTime = models.DateField(null=False)
    encharge = models.ForeignKey(User, on_delete=models.CASCADE)
    lastUpdate = models.DateTimeField(null=True)
    cost = models.FloatField(null=False, default=0)
    workDone = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(0)])
    skillNeed = models.ForeignKey(skill, on_delete=models.CASCADE)
    TaskName = models.CharField(max_length=300, null=False)
    Description = models.CharField(max_length=500, null=True)
    TaskID = models.ForeignKey(Task, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('manager_task_view', kwargs={'task_id': self.TaskID.id})


class Comment(models.Model):
    Subtask = models.ForeignKey(SubTask, related_name='comments', on_delete=models.CASCADE)
    user = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('SubTaskComment_view', kwargs={'id': self.Subtask.TaskID.id, 'my_id': self.Subtask.id})


class review(models.Model):
    ProjectName = models.CharField(max_length=300, null=False)
    Description = models.CharField(max_length=500, null=True)
    TaskReview = models.ForeignKey(Task, on_delete=models.CASCADE)


class Conclusions(models.Model):
    ProjectName = models.CharField(max_length=300, null=False)
    Description = models.CharField(max_length=500, null=True)
    UserCom = models.ForeignKey(User, on_delete=models.CASCADE)
    TaskReview = models.ForeignKey(Task, on_delete=models.CASCADE)


def subTaskMU(sender, instance, created, **kwargs):
    if created:
        tmp = Task.objects.filter(id=instance.TaskID.id)[0].cost
        Task.objects.filter(id=instance.TaskID.id).update(cost=tmp + instance.cost)


post_save.connect(subTaskMU, sender=SubTask)


def TaskMU(sender, instance, created, **kwargs):
    if created:
        if Sprint_Task.objects.filter(TaskId=instance.id):
            tmp = Sprint.objects.filter(id=Sprint_Task.objects.filter(TaskId=instance.id)[0].id)[0].cost
            Sprint.objects.filter(id=Sprint_Task.objects.filter(TaskId=instance.id)[0].id).update(
                cost=tmp + instance.cost)


post_save.connect(TaskMU, sender=Task)


def SprintMU(sender, instance, created, **kwargs):
    if created:
        tmp = project.objects.filter(id=instance.projectnum.id)[0].currentBudgeSchedule
        project.objects.filter(id=instance.projectnum.id).update(currentBudgeSchedule=tmp + instance.cost)


post_save.connect(SprintMU, sender=Sprint)


def SubTask_Update(sender, instance, update_fields, **kwargs):
    if SubTask.objects.filter(id=instance.id):
        tmp = Task.objects.filter(id=instance.TaskID.id)[0].cost
        tmpsub = SubTask.objects.filter(id=instance.id)[0].cost
        if tmpsub != instance.cost:
            dic = Task.objects.filter(id=instance.TaskID.id)[0]
            dic.cost = cost = tmp + instance.cost - tmpsub
            pre_save.send(sender=Task, instance=dic)
            Task.objects.filter(id=instance.TaskID.id).update(cost=tmp + instance.cost - tmpsub)


pre_save.connect(SubTask_Update, sender=SubTask)


def Task_Update(sender, instance, **kwargs):
    if Task.objects.filter(id=instance.id):
        if Sprint_Task.objects.filter(TaskId=instance.id):
            tmp = Sprint.objects.filter(id=Sprint_Task.objects.filter(TaskId=instance.id)[0].id)[0].cost
            tmpsub = Task.objects.filter(id=instance.id)[0].cost
            if tmpsub != instance.cost:
                dic = Sprint.objects.filter(id=Sprint_Task.objects.filter(TaskId=instance.id)[0].id)[0]
                dic.cost = tmp + instance.cost - tmpsub
                pre_save.send(sender=Sprint, instance=dic)
                Sprint.objects.filter(id=Sprint_Task.objects.filter(TaskId=instance.id)[0].id).update(
                    cost=tmp + instance.cost - tmpsub)
            # if instance.workDone==100:


pre_save.connect(Task_Update, sender=Task)


# def Sprint_Update(sender, instance, **kwargs):
#     if project.objects.filter(id=instance.projectnum.id):
#         tmp = project.objects.filter(id=instance.projectnum.id)[0].currentBudgeSchedule
#         tmpsub = Sprint.objects.filter(id=instance.id)[0].cost
#         if tmpsub != instance.cost:
#             project.objects.filter(id=instance.projectnum.id).update(currentBudgeSchedule=tmp + instance.cost - tmpsub)
#
#
# pre_save.connect(Sprint_Update, sender=Sprint)
