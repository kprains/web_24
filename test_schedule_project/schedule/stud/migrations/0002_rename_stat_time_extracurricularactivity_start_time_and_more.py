# Generated by Django 5.1.2 on 2024-10-27 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extracurricularactivity',
            old_name='stat_time',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='studyschedule',
            old_name='stat_time',
            new_name='start_time',
        ),
    ]