# Generated by Django 4.2.5 on 2023-09-28 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper_app', '0005_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='TrackerUser',
        ),
    ]
