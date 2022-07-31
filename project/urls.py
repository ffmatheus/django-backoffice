from django.contrib import admin
from django.urls import path, include
from department.views import DepartmentViewSet
from employee.views import EmployeeViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'department', DepartmentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('employee/', include('employee.urls')),
    path('department/', include('department.urls')),
    path('api/v1/', include(router.urls))
]
