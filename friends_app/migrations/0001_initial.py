# Generated by Django 5.1 on 2024-10-18 23:40

import config.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Создано')),
                ('is_published', models.BooleanField(default=False, help_text='Если уже неактуально, но может понадобиться, снимите флажок', verbose_name='Актуально на сайте')),
                ('name', models.CharField(help_text='Текст не более 255 символов', max_length=255, verbose_name='Название')),
                ('link', models.ImageField(blank=True, help_text='Добавьте Логотип (необязательно)', null=True, upload_to=config.utils.docs_path, verbose_name='Логотип')),
                ('description', models.TextField(help_text='Не более 70 символов', max_length=70, verbose_name='Чем была полезна:')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Создано')),
                ('is_published', models.BooleanField(default=False, help_text='Если уже неактуально, но может понадобиться, снимите флажок', verbose_name='Актуально на сайте')),
                ('name', models.CharField(help_text="Только буквы и ('-',) не более 100 символов ", max_length=100, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я-]+$')], verbose_name='Имя')),
                ('last_name', models.CharField(help_text="Только буквы и ('-',) не более 100 символов ", max_length=100, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я-]+$')], verbose_name='Фамилия')),
                ('sur_name', models.CharField(blank=True, help_text="Только буквы и (' ',) не более 100 символов (необязательно)", max_length=100, null=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я ]+$')], verbose_name='Отчество')),
                ('gender', models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], verbose_name='Категория')),
                ('description', models.TextField(help_text='Не более 70 символов', max_length=70, verbose_name='Роль в проекте')),
                ('link', models.ImageField(blank=True, help_text='Добавьте Фото (необязательно)', null=True, upload_to=config.utils.docs_path, verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Человека',
                'verbose_name_plural': 'Люди',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Только буквы и ('-',) не более 100 символов ", max_length=100, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я-]+$')], verbose_name='Имя')),
                ('last_name', models.CharField(help_text="Только буквы и ('-',) не более 100 символов ", max_length=100, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я-]+$')], verbose_name='Фамилия')),
                ('email', models.EmailField(help_text='Введите email: example@mail.com', max_length=254, verbose_name='email ')),
                ('link', models.ImageField(blank=True, help_text='Добавьте Фото (необязательно)', null=True, upload_to=config.utils.docs_path, verbose_name='Фото')),
                ('is_accept', models.BooleanField(default=False, help_text=None, verbose_name='Принято пользовательское соглашение')),
            ],
            options={
                'verbose_name': 'Волонтер',
                'verbose_name_plural': 'Волонтеры',
            },
        ),
    ]
