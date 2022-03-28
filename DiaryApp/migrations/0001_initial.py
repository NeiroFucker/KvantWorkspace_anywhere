# Generated by Django 3.1.5 on 2022-03-21 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CoreApp', '0001_initial'),
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KvantHomeTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'kvant_task',
            },
        ),
        migrations.CreateModel(
            name='KvantTaskMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('ОТ', 'ОТ'), ('УП', 'УП')], max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'lesson_mark',
            },
        ),
        migrations.CreateModel(
            name='KvantTaskBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('files', models.ManyToManyField(blank=True, to='CoreApp.FileStorage')),
                ('marks', models.ManyToManyField(blank=True, to='DiaryApp.KvantTaskMark')),
            ],
            options={
                'db_table': 'lesson_base',
            },
        ),
        migrations.CreateModel(
            name='KvantLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('base', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DiaryApp.kvanttaskbase')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.kvantcourse')),
                ('tasks', models.ManyToManyField(blank=True, to='DiaryApp.KvantHomeTask')),
            ],
            options={
                'db_table': 'kvant_lesson',
            },
        ),
        migrations.CreateModel(
            name='KvantHomeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('files', models.ManyToManyField(blank=True, to='CoreApp.FileStorage')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'task_work',
            },
        ),
        migrations.AddField(
            model_name='kvanthometask',
            name='base',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DiaryApp.kvanttaskbase'),
        ),
        migrations.AddField(
            model_name='kvanthometask',
            name='works',
            field=models.ManyToManyField(blank=True, to='DiaryApp.KvantHomeWork'),
        ),
    ]
