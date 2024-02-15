from django.urls import include, path
from . import views
from rest_framework import routers
from a_timesheet.views import EmployeeViewSet, MasterViewSet, EmployeeLoginView

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'master', MasterViewSet)


urlpatterns=[
  path('employee/login/', EmployeeLoginView.as_view(), name='employee-login'),
  path('',include(router.urls)),

]