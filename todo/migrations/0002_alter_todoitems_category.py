# Generated by Django 4.1.3 on 2022-12-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitems',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
