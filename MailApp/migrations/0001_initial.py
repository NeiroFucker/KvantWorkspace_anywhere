# Generated by Django 3.1.5 on 2022-02-20 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CoreApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MailReceiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mail_receivers',
            },
        ),
        migrations.CreateModel(
            name='KvantMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(default='Письмо', max_length=120)),
                ('files', models.ManyToManyField(blank=True, to='CoreApp.FileStorage')),
                ('receivers', models.ManyToManyField(to='MailApp.MailReceiver')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'kvant_messages',
                'ordering': ['-date', '-id'],
            },
        ),
        migrations.CreateModel(
            name='ImportantMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MailApp.kvantmessage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'important_mails',
            },
        ),
    ]
