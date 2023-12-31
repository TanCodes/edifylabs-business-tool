# Generated by Django 4.1.5 on 2023-05-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0005_invoice_total_amount_invoice_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="cgst_amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name="invoice",
            name="sgst_amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
