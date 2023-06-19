from django.contrib import admin
from django.db import transaction
from django.http import HttpResponse
from django.utils.html import format_html
from multiupload.fields import MultiFileField
from .models import Employee, Mission, File, MissionStockItem, StockItem
from django import forms


class MissionForm(forms.ModelForm):
    files = MultiFileField(min_num=0, max_num=10, max_file_size=1024 * 1024 * 5, required=False)

    class Meta:
        model = Mission
        fields = '__all__'


class MissionStockItemInline(admin.TabularInline):
    model = MissionStockItem


class MissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'start_zipcode', 'end_zipcode',
                    'distance', 'hotel_expenses', 'load_volume', 'category',
                    'toll_expenses', 'rental_expenses', 'get_employees', 'price_HT', 'result', 'get_files_display',
                    'get_items_summary']
    ordering = ['start_date']
    search_fields = ['name']
    form = MissionForm
    inlines = [MissionStockItemInline]
    filter_horizontal = ('stock_items',)

    def get_employees(self, obj):
        return ", ".join([f'{employee.first_name} {employee.last_name}' for employee in obj.employees.all()])

    get_employees.short_description = 'Employees'

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        if 'files' in form.cleaned_data:
            files = form.cleaned_data['files']
            for uploaded_file in files:
                File.objects.create(mission=form.instance, file=uploaded_file)

    def get_files_display(self, obj):
        files = File.objects.filter(mission=obj)
        if files:
            file_links = []
            for file in files:
                file_link = format_html(
                    '<a href="{}" target="_blank"><i class="fas fa-file"></i> {}</a>',
                    file.file.url,
                    file.file.name.split("/")[-1]
                )
                file_links.append(file_link)
            return format_html("<br>".join(file_links))
        return '-'

    get_files_display.short_description = 'Files'
    get_files_display.allow_tags = True

    def get_items_summary(self, obj):
        return obj.get_items_summary()

    def save_model(self, request, obj, form, change):
        with transaction.atomic():
            super().save_model(request, obj, form, change)
            mission_items = obj.missionstockitem_set.all()
            for mission_item in mission_items:
                stock_item = mission_item.stock_item
                stock_item.quantity -= mission_item.quantity
                if stock_item.quantity < 0:
                    return HttpResponse("Quantity < 0", status=403)
                else:
                    stock_item.save()

    class Media:
        css = {
            'all': ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css'],
        }


admin.site.register(Employee)
admin.site.register(Mission, MissionAdmin)
admin.site.register(StockItem)
