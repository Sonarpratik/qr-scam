# Generated by Django 4.1.3 on 2024-01-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_useraccount_is_customer_useraccount_is_super_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
