from django.contrib import admin
from django_celery_beat.models import PeriodicTask, IntervalSchedule

# Register your models here.
from .models import Task
admin.site.register(Task)