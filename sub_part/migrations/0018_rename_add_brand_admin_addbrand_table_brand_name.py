# Generated by Django 4.0.1 on 2022-02-08 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0017_admin_addbrand_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin_addbrand_table',
            old_name='add_brand',
            new_name='brand_name',
        ),
    ]