from django.contrib import admin
from .models import Employee, Task, Feedback, Meeting

class EmployeeList(admin.ModelAdmin):
    list_display = ('employee_number', 'name', 'city', 'email')
    list_filter = ('employee_number', 'name', 'city')
    search_fields = ('employee_number', 'name')
    ordering = ['employee_number']


class TaskList(admin.ModelAdmin):
    list_display = ('name', 'description', 'priority', 'deadline')
    list_filter = ('name', 'priority', 'deadline')
    search_fields = ('name', 'priority')
    ordering = ['name']


class FeedbackList(admin.ModelAdmin):
    list_display = ('emp_name', 'mang_name', 'message')
    list_filter = ('message','mang_name')
    search_fields = ('message','mang_name')
    ordering = ['message']


class MeetingList(admin.ModelAdmin):
  list_display = ('emp_name', 'mang_name', 'message')
  list_filter = ('message', 'mang_name')
  search_fields = ('message', 'mang_name')
  ordering = ['message']




admin.site.register(Employee, EmployeeList)
admin.site.register(Task, TaskList)
admin.site.register(Feedback, FeedbackList)
admin.site.register(Meeting, MeetingList)
