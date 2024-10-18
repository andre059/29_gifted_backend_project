# Generated by Django 5.1 on 2024-10-11 18:56

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0013_alter_registration_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='RU', verbose_name='Телефон'),
        ),
    ]