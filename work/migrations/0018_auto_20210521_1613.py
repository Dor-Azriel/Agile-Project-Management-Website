# Generated by Django 3.1.7 on 2021-05-21 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work', '0017_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sprint',
            name='projectnum',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='work.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subtask',
            name='subTasks',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='work.task'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='SpirntNum',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='work.sprint'),
            preserve_default=False,
        ),

    ]
