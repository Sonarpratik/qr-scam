# Generated by Django 4.1.3 on 2023-08-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_category_item_quantity_item_sqft_items_sqft_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageName', models.CharField(max_length=100, null=True)),
                ('tag', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]