# Generated by Django 4.2.2 on 2023-06-19 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "mission_app",
            "0020_alter_missionitem_mission_alter_missionitem_quantity_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="missionitem",
            name="quantity",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
