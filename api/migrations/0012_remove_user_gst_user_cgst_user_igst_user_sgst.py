# Generated by Django 4.1.3 on 2023-05-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_invoice_ack_date_invoice_ack_no_invoice_inr_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gst',
        ),
        migrations.AddField(
            model_name='user',
            name='cgst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='igst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sgst',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
