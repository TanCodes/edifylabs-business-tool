# Generated by Django 4.1.5 on 2023-05-21 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="invoice_number",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
