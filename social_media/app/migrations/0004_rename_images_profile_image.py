# Generated by Django 4.0.2 on 2022-02-21 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_like_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='images',
            new_name='image',
        ),
    ]