# Generated by Django 4.1.5 on 2023-05-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scheduler", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="scheduleclients",
            name="client_count",
            field=models.PositiveIntegerField(default=1),
        ),
    ]