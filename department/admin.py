from django.contrib import admin
from .models import Department

# Register your models here.
@admin.register(Department)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

