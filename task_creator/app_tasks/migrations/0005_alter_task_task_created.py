# Generated by Django 4.2.1 on 2023-06-03 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tasks', '0004_alter_task_task_created_alter_task_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 17, 50, 2, 345822, tzinfo=datetime.timezone.utc)),
        ),
    ]