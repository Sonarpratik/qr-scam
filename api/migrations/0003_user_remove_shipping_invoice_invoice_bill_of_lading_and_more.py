# Generated by Django 4.1.3 on 2023-05-10 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_invoice_singer_student_song_shipping_book_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_id', models.CharField(max_length=100)),
                ('Desc', models.CharField(max_length=100)),
                ('sac', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='invoice',
        ),
        migrations.AddField(
            model_name='invoice',
            name='bill_of_lading',
            field=models.CharField(default='dsfsd', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_address',
            field=models.CharField(default='sdfssdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_contact',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_gstin',
            field=models.CharField(default='dgffdg', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_pan',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='billing_state',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='brokername',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='buyers_order_no',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='dated',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='delivery_date',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='destination',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='dispatch_doc_no',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='dispatch_through',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='motor_v_no',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='other_ref',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='shipping_address',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='shipping_contact',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='shipping_gstin',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='shipping_pan',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='shipping_state',
            field=models.CharField(default='sdfsdfsdf', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Billing',
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
        migrations.AddField(
            model_name='user',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='api.invoice'),
        ),
    ]
