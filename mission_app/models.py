from django.db import models
from django.contrib.postgres.fields import ArrayField
from decimal import Decimal


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Mission(models.Model):
    CATEGORIES = [
        ('Movinga', 'Movinga'),
        ('Cocolis', 'Cocolis'),
        ('Categorie1', 'Categorie1'),
        ('Categorie2', 'Categorie2'),
        ('Categorie3', 'Categorie3'),
        ('Extrat', 'Extrat'),
        ('Fret', 'Fret'),
        ('Particulier', 'Particulier'),
        ('Odd', 'Odd'),
    ]

    name = models.CharField(max_length=255)
    price_HT = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    salary = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    start_zipcode = models.CharField(max_length=5, default=0)
    end_zipcode = models.CharField(max_length=5, default=0)
    distance = models.IntegerField()
    hotel_expenses = models.DecimalField(max_digits=7, decimal_places=2)
    load_volume = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.CharField(max_length=255, choices=CATEGORIES)
    toll_expenses = models.DecimalField(max_digits=7, decimal_places=2)
    rental_expenses = models.DecimalField(max_digits=7, decimal_places=2)
    employees = models.ManyToManyField(Employee, related_name='missions')
    file = models.FileField(upload_to='mission_files/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def result(self):
        result = self.price_HT - (self.salary + self.hotel_expenses + self.toll_expenses + self.rental_expenses + (
                Decimal(self.distance) * Decimal(0.3)))
        return round(result, 2)


class File(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='mission_files/', default='')
