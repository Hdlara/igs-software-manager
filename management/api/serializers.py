from rest_framework import serializers

from ..models import Employee


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
