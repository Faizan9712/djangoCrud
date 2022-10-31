from django.db import models


class Employee(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=20)
    emp_role = models.CharField(max_length=200)
    emp_salary = models.IntegerField()
    id = models.AutoField(auto_created=True, primary_key=True)

    def __str__(self):
        return self.emp_name
