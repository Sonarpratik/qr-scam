# Generated by Django 4.1.3 on 2023-07-11 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_items_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='quotation_number',
            field=models.CharField(blank=True, default='20', max_length=100, null=True),
        ),
    ]