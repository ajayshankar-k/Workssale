# Generated by Django 4.0.1 on 2022-02-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0036_admin_add_stock_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_add_purchase_tax_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_number', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('p_tax', models.CharField(max_length=100)),
                ('g_tot', models.CharField(max_length=100)),
                ('logger_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='admin_add_return_table',
            name='c_email',
            field=models.EmailField(max_length=254),
        ),
    ]