# Generated by Django 5.1 on 2024-10-20 09:00

import config.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0002_remove_eventlinkvideo_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='comment',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(1000, 'Комментарий не может быть длиннее 1000 символов.'), config.validators.validate_no_mixed_scripts, config.validators.validate_number_of_spaces_or_dashes, config.validators.validate_comment], verbose_name='Комментарий'),
        ),
    ]
