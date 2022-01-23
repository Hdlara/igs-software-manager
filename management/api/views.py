from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response

from .serializers import EmployeesSerializer
from ..models import Employee


class EmployeesViewSet(ListCreateAPIView):
    """
    List and create company
    """
    serializer_class = EmployeesSerializer

    def get_queryset(self):

        params = self.request.query_params
        queryset = Employee.objects.all()

        if 'name' in params:
            queryset = Employee.objects.filter(
                name__icontains=params['name']
            ).order_by("name")

        elif 'email' in params:
            queryset = Employee.objects.filter(
                email__icontains=params['email']
            ).order_by("email")

        elif 'department' in params:
            queryset = Employee.objects.filter(
                department__icontains=params['department']
            ).order_by("department")

        return queryset

    @method_decorator(transaction.atomic)
    def create(self, request):
        employees = request.data

        serializer = EmployeesSerializer(
            data=employees,
            many=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(employees, status=status.HTTP_201_CREATED)


class EmployeeDelete(DestroyAPIView):
    """
    delete employee
    """
    def destroy(self, request, **kwargs):
        try:
            employee = Employee.objects.get(
                name__iexact=kwargs.get('name'),
                email__iexact=kwargs.get('email'),
                department__iexact=kwargs.get('department')
            )

        except ObjectDoesNotExist:
            return Response(
                {"error": "There is no employee with these specifications."},
                status=status.HTTP_404_NOT_FOUND
            )
        Employee.objects.filter(
            name=employee.name,
            email=employee.email,
            department=employee.department,
        ).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
