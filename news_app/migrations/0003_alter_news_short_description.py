# Generated by Django 5.1 on 2024-10-02 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_alter_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='short_description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Краткое описание'),
        ),
    ]