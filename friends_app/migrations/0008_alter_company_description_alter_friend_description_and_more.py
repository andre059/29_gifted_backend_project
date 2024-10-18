# Generated by Django 5.1 on 2024-10-12 09:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends_app', '0007_merge_0006_friend_sur_name_0006_volunteer_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(help_text='Текст, не более 85 символов', max_length=85, verbose_name='Чем была полезна:'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='description',
            field=models.TextField(help_text='Текст, не более 85 символов', max_length=85, verbose_name='Роль в проекте'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='sur_name',
            field=models.CharField(blank=True, help_text="Только буквы и '-' не более 100 символов", max_length=100, null=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я-]+$')], verbose_name='Отчество'),
        ),
    ]