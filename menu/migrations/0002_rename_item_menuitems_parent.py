# Generated by Django 4.2 on 2023-04-13 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='item',
            new_name='parent',
        ),
    ]
