# Generated by Django 4.0.1 on 2022-02-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0037_admin_add_purchase_tax_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_add_expense_report_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('exp_category', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('logger_id', models.CharField(max_length=100)),
            ],
        ),
    ]