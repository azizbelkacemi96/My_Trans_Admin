# Generated by Django 4.2.2 on 2023-06-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mission_app", "0026_missionitem"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mission",
            name="stock_items",
        ),
        migrations.AddField(
            model_name="mission",
            name="items",
            field=models.ManyToManyField(
                related_name="missions",
                through="mission_app.MissionItem",
                to="mission_app.stock",
            ),
        ),
    ]
