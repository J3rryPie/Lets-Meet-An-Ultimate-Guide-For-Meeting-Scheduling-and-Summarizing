# Generated by Django 3.1.4 on 2021-06-01 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20210601_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meets',
            old_name='employee',
            new_name='e',
        ),
        migrations.RenameField(
            model_name='meets',
            old_name='meeting',
            new_name='m',
        ),
    ]