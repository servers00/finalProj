# Generated by Django 4.1.3 on 2022-12-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_task_smartname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='SMARTname',
        ),
        migrations.AddField(
            model_name='task',
            name='SMARTtask',
            field=models.CharField(max_length=200, null=True),
        ),
    ]