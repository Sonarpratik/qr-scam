# Generated by Django 4.1.3 on 2024-01-12 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_useraccount_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='is_super',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_customer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_superuser',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]