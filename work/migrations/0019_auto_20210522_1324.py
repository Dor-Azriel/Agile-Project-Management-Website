# Generated by Django 3.1.7 on 2021-05-22 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0018_auto_20210521_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='cost',
            field=models.FloatField(null=True),
        ),

    ]
