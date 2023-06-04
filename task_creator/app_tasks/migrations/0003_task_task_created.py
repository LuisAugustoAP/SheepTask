# Generated by Django 4.2.1 on 2023-06-03 16:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_tasks', '0002_alter_task_task_date_alter_task_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
