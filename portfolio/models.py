from django.db import models
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    employee_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.employee_number)




class Task(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=400, default='')
    priority = models.CharField(max_length=10, default='')
    deadline = models.DateField(default=timezone.now)
    created_date = models.DateField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.deadline = timezone.now()
        self.save()

    def __str__(self):
        return str(self.name)



class Feedback(models.Model):
    emp_name = models.CharField(max_length=50, default='')
    mang_name = models.CharField(max_length=50, default='')
    message = models.CharField(max_length=500, default='')
    requested_date = models.DateField(default=timezone.now)
    created_date = models.DateField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.requested_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.message)



class Meeting(models.Model):
  emp_name = models.CharField(max_length=50, default='')
  mang_name = models.CharField(max_length=50, default='')
  message = models.CharField(max_length=500, default='')
  requested_date = models.DateField(default=timezone.now)
  created_date = models.DateField(default=timezone.now, blank=True, null=True)

  def created(self):
    self.created_date = timezone.now()
    self.save()

  def updated(self):
    self.requested_date = timezone.now()
    self.save()

  def __str__(self):
    return str(self.message)
