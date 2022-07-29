from django.db import models
from department.models import Department
from django.core.validators import validate_email


class Employee(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(validators=[validate_email] ,max_length=256)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return super().__str__()

