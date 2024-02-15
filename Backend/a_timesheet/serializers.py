from rest_framework import serializers
from a_timesheet.models import Employee, Master

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"

class MasterSerializer(serializers.ModelSerializer):
        employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())    
        class Meta:
            model = Master
            fields = "__all__"

