# Generated by Django 5.1 on 2024-09-06 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0002_remove_project_preview_alter_project_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectimage',
            old_name='news',
            new_name='project',
        ),
    ]
