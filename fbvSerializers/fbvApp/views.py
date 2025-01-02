from django.shortcuts import render
from fbvApp.models import Employee,attendance,leave
from fbvApp.fbvSerializers import EmployeeSerializer,attendanceSerializer,leaveSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
 
@api_view(['GET', 'POST'])
def Employee_list(request):

    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data) # safe = False
    elif request.method == 'POST':
         serializer = EmployeeSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE']) 
def Employee_Update(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def attendance_list(request):

    if request.method == 'GET':
        attendances = attendance.objects.all()
        serializer = attendanceSerializer(attendances, many=True)
        return Response(serializer.data) # safe = False
    elif request.method == 'POST':
         serializer = attendanceSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def attendance_Update(request, pk):
    try:
        attendances = attendance.objects.get(pk=pk)
    except attendance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = attendanceSerializer(attendances)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = attendanceSerializer(attendances, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        attendances.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def leave_list(request):

    if request.method == 'GET':
        leaves = leave.objects.all()
        serializer = leaveSerializer(leaves, many=True)
        return Response(serializer.data) # safe = False
    elif request.method == 'POST':
         serializer = leaveSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def leave_Update(request, pk):
    try:
        leaves = leave.objects.get(pk=pk)
    except leave.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = leaveSerializer(leaves)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = leaveSerializer(leaves, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        leaves.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)