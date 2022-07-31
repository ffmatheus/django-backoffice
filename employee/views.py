from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Employee
from .forms import EmployeeForm
from .serializer import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer


class ListEmployeeView(ListView):
    model = Employee
    queryset = Employee.objects.all().order_by('name')

    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.GET.get("name") or None
        
        if name_filter:
            queryset = queryset.filter(name__contains=name_filter)

        return queryset

class CreateEmployeeView(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = '/employee/'

class UpdateEmployeeView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url = '/employee/'

class DeleteEmployeeView(DeleteView):
    model = Employee
    success_url = '/employee/'