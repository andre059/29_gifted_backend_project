# Generated by Django 5.1 on 2024-10-18 23:40

import config.utils
import config.validators
import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_event', models.CharField(help_text='Текст не более 300 символов', max_length=300, verbose_name='Название мероприятия')),
                ('description_of_event', models.TextField(help_text='Не более 2000 символов', max_length=2000, verbose_name='Описание мероприятия')),
                ('address_of_event', models.CharField(blank=True, help_text='Текст не более 500 символов', max_length=500, null=True, verbose_name='Адрес проведения мероприятия')),
                ('date_time_of_event', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время проведения мероприятия')),
                ('end_of_event', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время завершения мероприятия')),
            ],
            options={
                'verbose_name': 'мероприятие',
                'verbose_name_plural': 'мероприятия',
            },
        ),
        migrations.CreateModel(
            name='EventLinkVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_video', models.URLField(verbose_name='Ссылка на видео')),
                ('date', models.DateTimeField(verbose_name='Дата добавления')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_video', to='events_app.event')),
            ],
            options={
                'verbose_name': 'ссылка на видео мероприятия',
                'verbose_name_plural': 'ссылки на видео мероприятия',
            },
        ),
        migrations.CreateModel(
            name='EventPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ImageField(blank=True, help_text='Добавьте Фото мероприятия (необязательно)', null=True, upload_to=config.utils.docs_path, verbose_name='Фото мероприятия')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='events_app.event')),
            ],
            options={
                'verbose_name': 'фотография мероприятия',
                'verbose_name_plural': 'фотографии мероприятия',
            },
        ),
        migrations.CreateModel(
            name='EventVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.FileField(blank=True, help_text='Добавьте Видео мероприятия (необязательно)', null=True, upload_to=config.utils.docs_path, verbose_name='Видео мероприятия')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='events_app.event')),
            ],
            options={
                'verbose_name': 'видео мероприятия',
                'verbose_name_plural': 'видео мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(1, 'Имя должно быть не менее 1 символа'), django.core.validators.MaxLengthValidator(64, 'Имя должно быть не более 64 символов'), config.validators.validate_name_or_surname, config.validators.validate_no_mixed_scripts, config.validators.validate_number_of_spaces_or_dashes], verbose_name='Имя')),
                ('last_name', models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(1, 'Имя должно быть не менее 1 символа'), django.core.validators.MaxLengthValidator(64, 'Имя должно быть не более 64 символов'), config.validators.validate_name_or_surname, config.validators.validate_no_mixed_scripts, config.validators.validate_number_of_spaces_or_dashes], verbose_name='Фамилия')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Введите Телефон ', max_length=128, region='RU', verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.MaxLengthValidator(254, 'Email не может быть длиннее 254 символов'), config.validators.validate_email], verbose_name='Электронная почта')),
                ('comment', models.TextField(blank='True', validators=[django.core.validators.MaxLengthValidator(200, 'Комментарий не может быть длиннее 200 символов.'), config.validators.validate_no_mixed_scripts, config.validators.validate_number_of_spaces_or_dashes, config.validators.validate_comment], verbose_name='Комментарий')),
                ('timestamp', models.DateTimeField(verbose_name='Дата и время регистрации')),
                ('terms_agreed', models.BooleanField(default=False, help_text=None, verbose_name='Согласие с условиями')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='events_app.event', verbose_name='Мероприятие')),
            ],
            options={
                'verbose_name': 'Регистрация на мероприятие',
                'verbose_name_plural': 'Регистрация на мероприятия',
            },
        ),
    ]
