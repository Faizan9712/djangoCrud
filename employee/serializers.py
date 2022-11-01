from django.db.models import fields
from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "emp_name",
            "emp_email",
            "emp_contact",
            "emp_role",
            "emp_salary",
            "id",
        )
