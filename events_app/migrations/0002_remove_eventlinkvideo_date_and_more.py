# Generated by Django 5.1 on 2024-10-19 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventlinkvideo',
            name='date',
        ),
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время регистрации'),
        ),
    ]