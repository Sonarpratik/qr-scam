# Generated by Django 4.1.3 on 2023-05-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_rename_sac_user_product_id_remove_user_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sac',
            field=models.IntegerField(null=True),
        ),
    ]
