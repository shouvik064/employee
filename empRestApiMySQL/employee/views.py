from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def employee_list(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            employee = employee.filter(name__icontains=name)
        
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse(employee_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Employee.objects.all().delete()
        return JsonResponse({'message': '{} Employees were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    try: 
        employee = Employee.objects.get(pk=pk) 
    except Employee.DoesNotExist: 
        return JsonResponse({'message': 'The employee does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        employee_serializer = EmployeeSerializer(employee) 
        return JsonResponse(employee_serializer.data) 
 
    elif request.method == 'PUT': 
        employee_data = JSONParser().parse(request) 
        employee_serializer = EmployeeSerializer(employee, data=employee_data) 
        if employee_serializer.is_valid(): 
            employee_serializer.save() 
            return JsonResponse(employee_serializer.data) 
        return JsonResponse(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        employee.delete() 
        return JsonResponse({'message': 'Employee was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def employee_list_published(request):
    employee = Employee.objects.filter(published=True)
        
    if request.method == 'GET': 
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    
