# Generated by Django 4.2.2 on 2023-06-19 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mission_app", "0025_remove_stock_type_mission_stock_items"),
    ]

    operations = [
        migrations.CreateModel(
            name="MissionItem",
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
                ("quantity", models.PositiveIntegerField()),
                (
                    "mission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mission_app.mission",
                    ),
                ),
                (
                    "stock",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mission_app.stock",
                    ),
                ),
            ],
        ),
    ]