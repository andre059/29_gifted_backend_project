# Generated by Django 5.1 on 2024-09-01 17:53

import django.core.validators
import config.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Только буквы не более 50 символов', max_length=50, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я]+$')], verbose_name='Наименование проекта')),
                ('preview', models.ImageField(blank=True, null=True, upload_to=config.utils.docs_path, verbose_name='фотография')),
                ('content', models.TextField(blank=True, db_index=True, verbose_name='содержимое')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
