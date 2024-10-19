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
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('is_published', models.BooleanField(default=True, help_text='Если уже неактуально, но может понадобиться, снимите флажок', verbose_name='Актуально на сайте')),
                ('name', models.CharField(help_text='Текст не более 255 символов', max_length=255, verbose_name='Название')),
                ('category', models.CharField(choices=[('1', 'Документы'), ('2', 'Отчетность'), ('3', 'Уставные документы')], verbose_name='Категория')),
                ('link', models.FileField(help_text='Добавьте Документ ', upload_to=config.utils.docs_path, verbose_name='Документ')),
                ('description', models.TextField(help_text='Не более 1000 символов', max_length=1000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='OrganizationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('is_published', models.BooleanField(default=True, help_text='Если уже неактуально, но может понадобиться, снимите флажок', verbose_name='Актуально на сайте')),
                ('name', models.CharField(help_text='Текст не более 255 символов', max_length=255, verbose_name='Название')),
                ('legal_address', models.CharField(help_text='Текст не более 255 символов', max_length=255, verbose_name='Юридический адрес')),
                ('address', models.CharField(help_text='Текст не более 255 символов', max_length=255, verbose_name='Физический адрес')),
                ('ogrn_number', models.CharField(help_text='Состоит из 13 цифр', max_length=13, validators=[django.core.validators.RegexValidator(regex='\\d{13}')], verbose_name='ОГРН')),
                ('inn_number', models.CharField(help_text='Состоит из 10 цифр', max_length=10, validators=[django.core.validators.RegexValidator(regex='\\d{10}')], verbose_name='ИНН')),
                ('kpp_number', models.CharField(help_text='Состоит из 9 цифр', max_length=9, validators=[django.core.validators.RegexValidator(regex='\\d{9}')], verbose_name='КПП')),
                ('current_account', models.CharField(help_text='Состоит из 20 цифр', max_length=20, validators=[django.core.validators.RegexValidator(regex='\\d{20}')], verbose_name='Расчетный счет')),
                ('bik', models.CharField(help_text='Состоит из 9 цифр', max_length=9, validators=[django.core.validators.RegexValidator(regex='\\d{9}')], verbose_name='БИК')),
                ('correspondent_account', models.CharField(help_text='Состоит из 20 цифр', max_length=20, validators=[django.core.validators.RegexValidator(regex='\\d{20}')], verbose_name='Корр. счет')),
                ('director', models.CharField(help_text="Только буквы и ('-', ' ') не более 255 символов ", max_length=255, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я- ]+$')], verbose_name='ФИО директора')),
                ('link', models.ImageField(blank=True, help_text='Добавьте QR-код банка (необязательно)', null=True, upload_to=config.utils.docs_path, verbose_name='QR-код банка')),
            ],
            options={
                'verbose_name': 'Реквизиты организации',
                'verbose_name_plural': 'Реквизиты организации',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('is_published', models.BooleanField(default=True, help_text='Если уже неактуально, но может понадобиться, снимите флажок', verbose_name='Актуально на сайте')),
                ('name', models.CharField(help_text="Только буквы и ('-',) не более 100 символов ", max_length=100, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я-]+$')], verbose_name='Имя')),
                ('last_name', models.CharField(help_text="Только буквы и ('-',) не более 100 символов ", max_length=100, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я-]+$')], verbose_name='Фамилия')),
                ('surname', models.CharField(blank=True, help_text="Только буквы и (' ',) не более 100 символов (необязательно)", max_length=100, null=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я ]+$')], verbose_name='Отчество')),
                ('role', models.CharField(help_text='Текст не более 100 символов', max_length=100, verbose_name='Роль в проекте')),
                ('link', models.ImageField(blank=True, help_text='Добавьте Фото (необязательно)', null=True, upload_to=config.utils.docs_path, verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Члена команды',
                'verbose_name_plural': 'Члены команды',
            },
        ),
    ]
