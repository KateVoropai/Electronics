from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'position', 'is_active', 'network_element')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'position')
    list_filter = ('is_active', 'network_element')
