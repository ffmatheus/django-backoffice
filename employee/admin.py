from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    list_filter = ('department',)
    list_editable = ('email', 'department')
    search_fields = ('name', 'department')