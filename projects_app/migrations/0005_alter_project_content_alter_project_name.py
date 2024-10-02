# Generated by Django 5.1 on 2024-10-02 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0004_alter_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(blank=True, db_index=True, help_text='Только буквы не более 1000 символов', max_length=1000, verbose_name='содержимое'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(help_text='Только буквы не более 300 символов', max_length=300, verbose_name='Наименование проекта'),
        ),
    ]