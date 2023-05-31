# Generated by Django 4.1.3 on 2023-05-16 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_invoice_billing_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='ack_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='ack_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='inr_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gst',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gst_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='unit',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
