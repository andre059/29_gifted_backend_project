# Generated by Django 5.1 on 2024-09-23 15:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я]+$')], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я]+$')], verbose_name='Фамилия'),
        ),
    ]
