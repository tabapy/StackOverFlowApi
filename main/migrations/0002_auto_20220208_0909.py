# Generated by Django 3.1 on 2022-02-08 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='image',
            new_name='images',
        ),
    ]
