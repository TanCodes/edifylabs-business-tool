# Generated by Django 4.1.5 on 2023-05-02 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("clientsapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScheduleClients",
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
                ("first_name_S", models.CharField(max_length=100)),
                ("last_name_S", models.CharField(max_length=100)),
                ("review_call", models.BooleanField(default=False)),
                ("sessions", models.CharField(max_length=100)),
                ("my_time_field", models.TimeField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "coaching_type_course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clientsapp.course",
                    ),
                ),
            ],
        ),
    ]