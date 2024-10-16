# Generated by Django 5.1 on 2024-09-06 13:39

import django.core.validators
import django.db.models.deletion
import config.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='preview',
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(help_text='Только буквы не более 50 символов', max_length=300, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Zа-яА-Я]+$')], verbose_name='Наименование проекта'),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ImageField(upload_to=config.utils.docs_path, verbose_name='Изображение')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects_app.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
