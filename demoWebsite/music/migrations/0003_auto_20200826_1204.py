# Generated by Django 3.1 on 2020-08-26 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20200826_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='is_favourite',
            new_name='is_favorite',
        ),
    ]