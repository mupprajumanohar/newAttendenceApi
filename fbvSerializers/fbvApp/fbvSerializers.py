from rest_framework import serializers
from fbvApp.models import Employee, attendance, leave


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = '__all__'

class leaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = leave
        fields = '__all__'