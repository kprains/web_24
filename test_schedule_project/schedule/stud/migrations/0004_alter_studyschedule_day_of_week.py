# Generated by Django 5.1.2 on 2024-10-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud', '0003_alter_extracurricularactivity_activity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyschedule',
            name='day_of_week',
            field=models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=10),
        ),
    ]
