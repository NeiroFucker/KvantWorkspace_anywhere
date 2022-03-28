# Generated by Django 3.1.5 on 2022-03-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvantcourseshedule',
            name='week_day',
            field=models.CharField(choices=[('ПН', 'Понедельник'), ('ВТ', 'Вторник'), ('СР', 'Среда'), ('ЧТ', 'Четверг'), ('ПТ', 'Пятница'), ('СБ', 'Суббота'), ('ВС', 'Воскресенье')], max_length=20),
        ),
    ]
