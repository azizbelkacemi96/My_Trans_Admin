from django.contrib import admin
from django.utils.html import format_html
from multiupload.fields import MultiFileField
from .models import Employee, Mission, File
from django import forms


class MissionForm(forms.ModelForm):
    files = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)

    class Meta:
        model = Mission
        fields = '__all__'


class MissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'start_zipcode', 'end_zipcode',
                    'distance', 'hotel_expenses', 'load_volume', 'category',
                    'toll_expenses', 'rental_expenses', 'get_employees', 'price_HT', 'result', 'get_files_display']
    ordering = ['start_date']
    search_fields = ['name']
    form = MissionForm

    def get_employees(self, obj):
        return ", ".join([f'{employee.first_name} {employee.last_name}' for employee in obj.employees.all()])

    get_employees.short_description = 'Employees'

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        if 'file' in form.cleaned_data:
            files = request.FILES.getlist('file')
            for file in files:
                File.objects.create(mission=form.instance, file=file)

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

    class Media:
        css = {
            'all': ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css'],
        }


admin.site.register(Employee)
admin.site.register(Mission, MissionAdmin)
