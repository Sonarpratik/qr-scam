# Generated by Django 4.1.3 on 2023-05-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_invoice_terms_of_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorys',
            name='total_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
