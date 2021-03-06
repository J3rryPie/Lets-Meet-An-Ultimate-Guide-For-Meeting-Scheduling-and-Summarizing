# Generated by Django 3.1.4 on 2021-06-01 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_meeting_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='color',
            field=models.CharField(default='Black', max_length=10),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
