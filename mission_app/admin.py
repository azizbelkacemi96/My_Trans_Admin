from django.contrib import admin
from .models import Employee, Mission


class MissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'start_zipcode', 'end_zipcode',
                    'distance', 'hotel_expenses', 'load_volume', 'category',
                    'toll_expenses', 'rental_expenses', 'get_employees', 'price_HT', 'result']
    ordering = ['start_date']
    search_fields = ['name']

    def get_employees(self, obj):
        return ", ".join([f'{employee.first_name} {employee.last_name}' for employee in obj.employees.all()])

    get_employees.short_description = 'Employees'


admin.site.register(Employee)
admin.site.register(Mission, MissionAdmin)
