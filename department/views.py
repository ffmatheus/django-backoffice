from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Department
from .forms import DepartmentForm
from .serializer import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer


class ListDepartmentView(ListView):
    model = Department
    queryset = Department.objects.all().order_by('name')

    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.GET.get("name") or None
        
        if name_filter:
            queryset = queryset.filter(name__contains=name_filter)

        return queryset

class CreateDepartmentView(CreateView):
    model = Department
    form_class = DepartmentForm
    success_url = '/department/'

class UpdateDepartmentView(UpdateView):
    model = Department
    form_class = DepartmentForm
    success_url = '/department/'

class DeleteDepartmentView(DeleteView):
    model = Department
    success_url = '/department/'