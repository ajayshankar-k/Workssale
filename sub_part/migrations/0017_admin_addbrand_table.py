# Generated by Django 4.0.1 on 2022-02-08 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0016_rename_add_customer_table_admin_add_customer_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_addbrand_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_brand', models.CharField(max_length=100)),
            ],
        ),
    ]
