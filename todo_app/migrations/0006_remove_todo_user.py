# Generated by Django 5.0.4 on 2024-04-28 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
