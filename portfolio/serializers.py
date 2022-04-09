from rest_framework import serializers
from .models import Employee, Task, Feedback, Meeting


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
            model = Employee

            fields = ('pk','name','employee_number' , 'city', 'state', 'email')

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
            model = Task
            fields = ('pk', 'name', 'description', 'priority', 'deadline')


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
            model = Feedback
            fields = ('pk','emp_name', 'mang_name', 'message', 'created_date')


class MeetingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meeting
    fields = ('pk', 'emp_name', 'mang_name', 'message', 'created_date')
