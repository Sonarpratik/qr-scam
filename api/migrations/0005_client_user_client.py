# Generated by Django 4.1.3 on 2023-07-08 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_items_unit_quotation_client_id_quotation_user_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user_client',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
