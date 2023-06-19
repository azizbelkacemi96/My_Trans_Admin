# Generated by Django 4.2.2 on 2023-06-19 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mission_app", "0019_rename_quantity_used_missionitem_quantity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="missionitem",
            name="mission",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="mission_app.mission"
            ),
        ),
        migrations.AlterField(
            model_name="missionitem",
            name="quantity",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="missionitem",
            name="stock_item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="mission_app.stockitem"
            ),
        ),
    ]
