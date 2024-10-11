# Generated by Django 5.1 on 2024-10-03 16:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_alter_contactpage_address_alter_contactpage_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='for_media',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='header',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='short_description',
        ),
        migrations.AddField(
            model_name='contactpage',
            name='email_for_media',
            field=models.EmailField(default='darserdca54@gmail.com', help_text='Укажите электронную почту для СМИ', max_length=200, verbose_name='Электронная почта для СМИ'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='phone_for_media',
            field=models.CharField(default='+7‒962‒836‒86‒48', help_text='Телефоны для СМИ', max_length=255, verbose_name='Телефон для СМИ'),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='phones',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(help_text='Номер телефона', max_length=255, verbose_name='Телефон'), size=None),
        ),
    ]