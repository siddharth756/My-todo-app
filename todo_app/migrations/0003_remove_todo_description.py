# Generated by Django 5.0.3 on 2024-04-25 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_remove_todo_date_remove_todo_todo_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
    ]
