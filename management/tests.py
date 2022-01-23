from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from management.api.serializers import EmployeesSerializer


class EmployeesViewSetTestCase(APITestCase):

    def test_view_returns_200_valid_registration(self):
        """
        Test for creating a new employee.
        """
        url = reverse('employee')
        data = {
            'name': 'henrique dias lara',
            'email': 'henriquediaslara@hotmail.com',
            'department': 'development'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_view_search_returns_all_employees(self):
        """
        tests search employees to return all.
        """
        url = reverse('employee')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_search_employees_by_name(self):
        """
        tests search employees by name.
        """
        url = 'http://127.0.0.1:8000/employee?name=henrique'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_search_employees_by_email(self):
        """
        tests search employees by email.
        """
        url = 'http://127.0.0.1:8000/' \
              'employee?email=henriquediaslara@hotmail.com'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_search_employees_by_department(self):
        """
        tests search employees by department.
        """
        url = 'http://127.0.0.1:8000/employee?department=development'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EmployeesSerializerTestCase(APITestCase):

    data = {
        'name': 'henrique dias lara',
        'email': 'test',
        'department': 'development'
    }

    data_valid = {
        'name': 'henrique dias lara',
        'email': 'test@hotmail.com',
        'department': 'development'
    }

    def test_serializer_invalid_email_registration(self):
        """
        Test test invalid email on registration.
        """
        serializer = EmployeesSerializer(
            data=self.data
        )

        self.assertFalse(serializer.is_valid())

    def test_serializer_validation_of_fields_to_add_employee(self):
        """
        test the inclusion of an employee in the serializer
        """
        serializer = EmployeesSerializer(
            data=self.data_valid
        )

        self.assertTrue(serializer.is_valid())
