from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=15)

    def __str__(self):
        return f'{department_name}'

class Employee(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone_number = models.IntegerField()
    start_day_of_work = models.DateField()

    def __str__(self):
        return f'{first_name}-{last_name}-{email}-{phone_number}-{start_day_of_work}'

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='job')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='job')