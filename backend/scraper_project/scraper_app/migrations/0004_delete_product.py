# Generated by Django 4.2.5 on 2023-09-28 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper_app', '0003_alter_scrapedproduct_link_productdetail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
