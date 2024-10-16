# Generated by Django 5.1 on 2024-10-16 20:16

import config.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0006_alter_project_content_alter_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(help_text='Не более 1000 символов', max_length=1000, verbose_name='Описание проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(help_text='Текст не более 255 символов', max_length=255, verbose_name='Название проекта'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='link',
            field=models.ImageField(help_text='Добавьте Изображение ', upload_to=config.utils.docs_path, verbose_name='Изображение'),
        ),
    ]
