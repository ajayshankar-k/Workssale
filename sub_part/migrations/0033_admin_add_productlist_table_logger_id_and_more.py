# Generated by Django 4.0.1 on 2022-02-14 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0032_admin_add_customer_table_logger_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_add_productlist_table',
            name='logger_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin_add_vendor_table',
            name='logger_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin_addbrand_table',
            name='logger_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin_addtax_table',
            name='logger_id',
            field=models.CharField(default=11, max_length=200),
            preserve_default=False,
        ),
    ]
