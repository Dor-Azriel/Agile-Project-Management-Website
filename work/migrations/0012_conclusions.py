# Generated by Django 3.1.7 on 2021-04-27 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work', '0011_subtask_workdone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conclusions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName', models.CharField(max_length=300)),
                ('Description', models.CharField(max_length=500, null=True)),
                ('TaskReview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.task')),
                ('UserCom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
