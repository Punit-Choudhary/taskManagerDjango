from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length = 60)
    task_note = models.TextField()
    start_on = models.DateField(null=True, blank=True)
    start_at = models.TimeField(null=True, blank=True)
    point = models.IntegerField(null=True, blank=True)
    end_on = models.DateField(null=True, blank=True)
    end_at = models.TimeField(null=True, blank=True)
    is_completed = models.BooleanField(default = False)
    def __str__(self):
        return self.task_name