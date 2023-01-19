from rest_framework import serializers
from .models import Department, Job, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            "id",
            "department_name",
        )

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
class JobSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(required=False)
    department = serializers.StringRelatedField()
    department_id = serializers.IntegerField()
    user = serializers.StringRelatedField()
    class Meta:
        model = Job
        fields = (
            "id",
            "department",
            "department_id",
            "user",
            "employee"
        )
    
    def create(self, validated_data):
        employee_data = validated_data.pop("employee")
        validated_data["user_id"] = self.context["request"].user.id
        job = Job.objects.create(**validated_data)

        for employee in employee_data:
            emp = Employee.objects.create(**employee)
            job.employee.add(emp)

        job.save()
        return job

class StaffSerializer(serializers.ModelSerializer):
    job = JobSerializer(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ('id', 'department_name', 'job')
        