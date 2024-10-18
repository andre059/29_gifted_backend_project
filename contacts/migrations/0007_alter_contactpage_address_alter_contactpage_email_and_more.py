# Generated by Django 5.1 on 2024-10-15 07:25

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_alter_contactpage_phone_1_alter_contactpage_phone_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='address',
            field=models.CharField(help_text='Текст не более 255 символов', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='email',
            field=models.EmailField(help_text='Введите email: example@mail.com', max_length=254, verbose_name='email '),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='email_for_media',
            field=models.EmailField(help_text='Введите email: example@mail.com', max_length=254, verbose_name='email  для СМИ'),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='phone_1',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Введите Первый номер телефона ', max_length=128, region='RU', verbose_name='Первый номер телефона'),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='phone_2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Введите Второй номер телефона (необязательно)', max_length=128, null=True, region='RU', verbose_name='Второй номер телефона'),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='phone_for_media',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Введите Телефон для СМИ ', max_length=128, region='RU', verbose_name='Телефон для СМИ'),
        ),
    ]