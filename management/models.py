from django.db import models
from uuid import uuid4


class Employee(models.Model):
    id_employee = models.UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('E-mail', max_length=50)
    department = models.CharField('Departament', max_length=50)
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('name', 'email', 'department')
