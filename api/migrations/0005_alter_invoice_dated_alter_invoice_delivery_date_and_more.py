# Generated by Django 4.1.3 on 2023-05-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_user_desc_alter_user_desc_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='dated',
            field=models.DateTimeField(max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='delivery_date',
            field=models.DateTimeField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='desc_id',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='quantity',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rate',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sac',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
