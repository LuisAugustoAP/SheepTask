from django.db import models
from django.utils import timezone as tmz
from datetime import datetime, timedelta, timezone

class task(models.Model):
    task_name = models.CharField(max_length=50)
    task_date = models.DateTimeField()
    task_created = models.DateTimeField(default=tmz.now())
    task_status = models.CharField(max_length=20, default="Em Andamento")
