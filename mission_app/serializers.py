from rest_framework import serializers
from .models import Employee, Mission


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name"]


class MissionSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = Mission
        fields = [
            "id",
            "name",
            "start_date",
            "end_date",
            "start_location",
            "end_location",
            "distance",
            "hotel_expenses",
            "load_volume",
            "category",
            "toll_expenses",
            "rental_expenses",
            "employees",
            "price_HT",
        ]
