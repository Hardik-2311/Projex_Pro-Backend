# Generated by Django 4.2.5 on 2023-11-05 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='project',
            new_name='project_id',
        ),
    ]