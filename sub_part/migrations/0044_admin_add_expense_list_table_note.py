# Generated by Django 4.0.1 on 2022-02-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0043_admin_add_expense_list_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_add_expense_list_table',
            name='note',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
