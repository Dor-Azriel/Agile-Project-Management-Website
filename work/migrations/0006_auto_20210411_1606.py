# Generated by Django 3.1.7 on 2021-04-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_auto_20210411_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='language',
            field=models.CharField(choices=[(1, 'Java'), (2, 'C'), (3, 'C++'), (4, 'Python'), (5, 'C#'), (6, 'React'), (7, 'HTML'), (8, 'php'), (9, 'DB')], default='Java', max_length=10),
        ),
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(choices=[(1, 'Junior'), (2, 'Senior'), (3, 'expert')], default='Junior', max_length=10),
        ),
    ]
