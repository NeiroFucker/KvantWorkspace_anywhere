# Generated by Django 3.1.5 on 2022-03-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvanttaskbase',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
