# Generated by Django 4.1.3 on 2023-05-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_rename_user_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='client_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]