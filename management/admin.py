from django.contrib import admin

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('name', 'email', 'department', 'create_at')


admin.site.register(Employee, EmployeeAdmin)
