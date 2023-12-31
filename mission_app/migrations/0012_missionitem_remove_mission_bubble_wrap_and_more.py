# Generated by Django 4.2.2 on 2023-06-19 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mission_app", "0011_carton_mission_bubble_wrap_mission_straps_and_more"),
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
                ("quantity_used", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name="mission",
            name="bubble_wrap",
        ),
        migrations.RemoveField(
            model_name="mission",
            name="cartons",
        ),
        migrations.RemoveField(
            model_name="mission",
            name="straps",
        ),
        migrations.AddField(
            model_name="stockitem",
            name="type",
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name="stockitem",
            name="name",
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.DeleteModel(
            name="Carton",
        ),
        migrations.AddField(
            model_name="missionitem",
            name="mission",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="mission_app.mission"
            ),
        ),
        migrations.AddField(
            model_name="missionitem",
            name="stock_item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="mission_app.stockitem"
            ),
        ),
        migrations.AddField(
            model_name="mission",
            name="items",
            field=models.ManyToManyField(
                through="mission_app.MissionItem", to="mission_app.stockitem"
            ),
        ),
    ]
