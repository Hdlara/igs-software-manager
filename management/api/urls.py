from django.urls import path

from .views import EmployeesViewSet, EmployeeDelete

urlpatterns = [
    path(
        'employee',
        EmployeesViewSet.as_view(),
        name='employee'
    ),

    path(
        'employee-delete/<str:name>/<str:email>/<str:department>',
        EmployeeDelete.as_view(),
        name='delete-employee'
    )
]
