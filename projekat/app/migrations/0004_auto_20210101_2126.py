# Generated by Django 3.1.4 on 2021-01-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201230_1823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['due_date']},
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='owner',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2021-01-01'),
        ),
    ]
