# Generated by Django 5.1.3 on 2024-12-24 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_task_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
