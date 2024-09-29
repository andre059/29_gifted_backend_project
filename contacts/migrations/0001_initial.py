# Generated by Django 5.1 on 2024-09-24 09:30

import contacts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('photo', models.ImageField(upload_to=contacts.models.docs_path, verbose_name='Фото')),
                ('short_description', models.TextField(verbose_name='Краткое описание')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phones', models.CharField(max_length=255, verbose_name='Телефоны')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('for_media', models.CharField(max_length=255, verbose_name='Для СМИ')),
            ],
            options={
                'verbose_name': 'Страница контактов',
                'verbose_name_plural': 'Страницы контактов',
            },
        ),
    ]