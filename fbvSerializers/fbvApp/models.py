from django.db import models
from django.utils import timezone
from datetime import date


# Create your models here.

class Employee(models.Model):
    Id = models.AutoField(primary_key=True)
    employeeId = models.CharField(max_length=15)
    employeename = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phonenumber = models.BigIntegerField()
    address = models.CharField(max_length=200)
    jobtitle = models.CharField(max_length=100)
    joingdate = models.DateField()
    leaves = models.IntegerField()
    status = models.IntegerField()

    #def __str__(self):
     #   return self.employeename+self.employeeId+self.jobtitle+self.leaves+self.status

class attendance(models.Model):
    Id = models.AutoField(primary_key=True)
    employeeId = models.CharField(max_length=15)
    attendencestatus = models.CharField(max_length=15)
    date = models.DateTimeField()
    daystatus = models.CharField(max_length=15)
    status = models.IntegerField()
    time = models.TimeField(default=timezone.now)

   # def __str__(self):
    #    return self.employeeId+self.attendencestatus+self.date+self.daystatus+self.status+self.time
    
class leave(models.Model):
    Id = models.AutoField(primary_key=True)
    employeeId = models.CharField(max_length=15)
    fromdate = models.DateField()
    todate = models.DateField()
    reason = models.CharField(max_length=1000)
    discription = models.CharField(max_length=750)
    status = models.IntegerField()

    # def __str__(self):
    #     return self.employeeId+self.fromdate+self.todate+self.reason+self.discription+self.status