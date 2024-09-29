# Generated by Django 5.1 on 2024-09-29 09:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_alter_developer_first_name_alter_developer_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='surname',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я]+$')], verbose_name='Отчество'),
        ),
    ]
