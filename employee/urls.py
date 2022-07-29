from django.urls import path
from .views import ListEmployeeView, CreateEmployeeView, UpdateEmployeeView, DeleteEmployeeView

urlpatterns = [
    path('', ListEmployeeView.as_view(), name='employee.index'),
    path('create/', CreateEmployeeView.as_view() , name='employee.create'),
    path('update/<int:pk>', UpdateEmployeeView.as_view() , name='employee.update'),
    path('delete/<int:pk>', DeleteEmployeeView.as_view() , name='employee.delete')
]