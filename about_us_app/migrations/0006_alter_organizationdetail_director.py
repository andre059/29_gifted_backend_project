# Generated by Django 5.1 on 2024-09-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us_app', '0005_organizationdetail_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationdetail',
            name='director',
            field=models.CharField(default='Иванов Иван Иванович', help_text='Только буквы не более 50 символов', max_length=200, verbose_name='ФИО директора'),
        ),
    ]
