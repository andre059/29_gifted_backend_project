# Generated by Django 5.1 on 2024-10-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0005_alter_eventvideo_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlinkvideo',
            name='link_video',
            field=models.URLField(help_text='Введите ссылку, не более 255 символов', max_length=255, verbose_name='Ссылка на видео'),
        ),
    ]
