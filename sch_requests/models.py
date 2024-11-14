from django.db import models
from family.models import *

# Create your models here.
class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=15)

class DetailWork(models.Model):
    work_id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="detail_works")
    work_name = models.CharField(max_length=15)

class FamilySchedule(models.Model):
    fam_schedule = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="family_schedules")
    schedule_start_time = models.DateTimeField()
    schedule_end_time = models.DateTimeField()
    schedule_title = models.CharField(max_length=15)
    schedule_memo = models.CharField(max_length=50, blank=True, null=True)
    is_daily = models.BooleanField(default=False)
    is_weekly = models.BooleanField(default=False)
    is_monthly = models.BooleanField(default=False)
    is_yearly = models.BooleanField(default=False)

class Request(models.Model):
    family = models.ForeignKey(FamilyInfo, on_delete=models.CASCADE)
    fam_schedule = models.ForeignKey(FamilySchedule, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)