from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from employees.serializers import EmployeeSerializer
from employees.models import Employee
from employees.permissions import IsActiveEmployee


class EmployeeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = (IsAuthenticated, IsActiveEmployee,)
