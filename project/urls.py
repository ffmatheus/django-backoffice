from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from department.views import DepartmentViewSet
from employee.views import EmployeeViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet, basename="employee.api")
router.register(r'department', DepartmentViewSet, basename="department.api")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('employee/', include('employee.urls')),
    #path('department/', include('department.urls')),
    path('api/v1/', include((router.urls, 'api'), namespace='api-root')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
