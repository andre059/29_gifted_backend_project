# Generated by Django 5.1 on 2024-10-18 23:40

import config.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('title', models.CharField(help_text='Текст не более 300 символов', max_length=300, verbose_name='Заголовок')),
                ('content', models.TextField(help_text='Не более 1300 символов', max_length=1300, verbose_name='Содержание')),
                ('video', models.URLField(blank=True, null=True, verbose_name='Видео')),
                ('short_description', models.TextField(help_text='Не более 1000 символов', max_length=1000, verbose_name='Краткое описание')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ImageField(blank=True, help_text='Добавьте Изображение (необязательно)', null=True, upload_to=config.utils.docs_path, verbose_name='Изображение')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='news_app.news', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
