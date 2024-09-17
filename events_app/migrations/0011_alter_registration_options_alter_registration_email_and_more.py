# Generated by Django 5.1 on 2024-09-11 12:38

import django.core.validators
import events_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0010_event_end_of_event_alter_event_date_time_of_event_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'verbose_name': 'Регистрация на мероприятие', 'verbose_name_plural': 'Регистрация на мероприятия'},
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.MaxLengthValidator(254, 'Email не может быть длиннее 254 символов'), events_app.validators.validate_email], verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='first_name',
            field=models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(1, 'Имя должно быть не менее 1 символа'), django.core.validators.MaxLengthValidator(64, 'Имя должно быть не более 64 символов'), events_app.validators.validate_name_or_surname, events_app.validators.validate_no_mixed_scripts], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='last_name',
            field=models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(1, 'Фамилия должна быть не менее 1 символа'), django.core.validators.MaxLengthValidator(64, 'Фамилия должна быть не более 64 символов'), events_app.validators.validate_name_or_surname, events_app.validators.validate_no_mixed_scripts], verbose_name='Фамилия'),
        ),
    ]