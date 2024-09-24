from django.contrib import admin

from network.models import NetworkElement


@admin.register(NetworkElement)
class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'debit', 'supplier')
    search_fields = ('city',)
    actions = ['clear_debit']

    def clear_debit(self, request, queryset):
        queryset.update(debit=0)
    clear_debit.short_description = 'Очистить задолженность'
