# Generated by Django 4.0.1 on 2022-02-08 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0019_admin_addtax_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_add_productlist_table',
            name='product_category',
        ),
        migrations.RemoveField(
            model_name='admin_add_productlist_table',
            name='product_description',
        ),
        migrations.RemoveField(
            model_name='admin_add_productlist_table',
            name='product_purchase_price',
        ),
        migrations.RemoveField(
            model_name='admin_add_productlist_table',
            name='product_sku',
        ),
        migrations.RemoveField(
            model_name='admin_add_productlist_table',
            name='product_tax',
        ),
    ]