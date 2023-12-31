# Generated by Django 4.1.2 on 2023-06-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Mission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "price_HT",
                    models.DecimalField(decimal_places=2, default=0, max_digits=7),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("start_location", models.CharField(max_length=255)),
                ("end_location", models.CharField(max_length=255)),
                ("distance", models.IntegerField()),
                ("hotel_expenses", models.DecimalField(decimal_places=2, max_digits=7)),
                ("load_volume", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Moving", "Moving"),
                            ("Cocolis", "Cocolis"),
                            ("Categorie1", "Categorie1"),
                            ("Categorie2", "Categorie2"),
                            ("Categorie3", "Categorie3"),
                            ("Extrat", "Extrat"),
                            ("Fret", "Fret"),
                            ("Particulier", "Particulier"),
                            ("Odd", "Odd"),
                        ],
                        max_length=255,
                    ),
                ),
                ("toll_expenses", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "rental_expenses",
                    models.DecimalField(decimal_places=2, max_digits=7),
                ),
                (
                    "employees",
                    models.ManyToManyField(
                        related_name="missions", to="mission_app.employee"
                    ),
                ),
            ],
        ),
    ]
