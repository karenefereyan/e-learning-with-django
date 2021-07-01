from django.db import models
from administrator.models import *
# Create your models here.


class Staff(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class CourseAllocation(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)  # * Approved by admin
