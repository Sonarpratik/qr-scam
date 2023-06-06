# Generated by Django 4.1.3 on 2023-06-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_useraccount_create_useraccount_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='USERNAME_FIELD',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='last_name',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='create',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='view',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
