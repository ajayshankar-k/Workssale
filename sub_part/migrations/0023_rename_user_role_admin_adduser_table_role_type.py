# Generated by Django 4.0.1 on 2022-02-09 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0022_remove_admin_add_customer_table_customer_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin_adduser_table',
            old_name='user_role',
            new_name='role_type',
        ),
    ]