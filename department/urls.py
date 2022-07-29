from django.urls import path
from .views import ListDepartmentView, CreateDepartmentView, UpdateDepartmentView, DeleteDepartmentView

urlpatterns = [
    path('', ListDepartmentView.as_view(), name='department.index'),
    path('create/', CreateDepartmentView.as_view() , name='department.create'),
    path('update/<int:pk>', UpdateDepartmentView.as_view() , name='department.update'),
    path('delete/<int:pk>', DeleteDepartmentView.as_view() , name='department.delete')
]