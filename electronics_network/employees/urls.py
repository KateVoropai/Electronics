from rest_framework import routers

from employees.views import EmployeeViewSet


router = routers.SimpleRouter()
router.register("employee", EmployeeViewSet, basename="Employee")

urlpatterns = router.urls
