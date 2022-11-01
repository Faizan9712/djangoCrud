from email.policy import HTTP
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .models import Employee
from .forms import EmployeeForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
from rest_framework import serializers


@api_view(["GET"])
def employees_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many="True")
    try:
        if serializer:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def create_employee(request):
    employee = EmployeeSerializer(data=request.data)
    if Employee.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This data already exists")
    if employee.is_valid():
        employee.save()
        return Response(employee.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# def create_employee(request):
#     form = EmployeeForm()
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("employees-list")

#     context = {
#         "form": form,
#     }
#     return render(request, "employee/create.html", context.data)


@api_view(["PUT"])
def edit_employee(request, pk):
    try:
        employee = Employee.objects.get(id=pk)
        if employee:
            serializer = EmployeeSerializer(instance=employee, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                print(serializer.data)
                print("Error hai yaaar")
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Something went wrong")
    except:
        return Response("No employee with id = " + pk)

    # def edit_employee(request, pk):
    # employee = Employee.objects.get(id=pk)
    # form = EmployeeForm(instance=employee)

    # if request.method == "POST":
    #     form = EmployeeForm(request.POST, instance=employee)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("employees-list")

    # context = {
    #     "employee": employee,
    #     "form": form,
    # }
    # return render(request, "employee/edit.html", context)


@api_view(["DELETE"])
def delete_employee(request, pk):
    try:
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return Response("Employee deleted with id = " + pk)
    except:
        return Response("No employee with id = " + pk)


# employee = Employee.objects.get(id=pk)
# if request.method == "POST":
#     employee.delete()
#     return redirect("employees-list")

# context = {
#     "employee": employee,
# }
# return render(request, "employee/delete.html", context)
