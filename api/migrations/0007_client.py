# Generated by Django 4.1.3 on 2023-05-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_invoice_dated_alter_invoice_delivery_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('gst_no', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('shipping_address', models.CharField(max_length=100)),
                ('billing_address', models.CharField(max_length=100)),
            ],
        ),
    ]
