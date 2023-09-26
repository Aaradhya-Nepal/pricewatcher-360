# Generated by Django 4.2.5 on 2023-09-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('current_price', models.CharField(max_length=20)),
                ('original_price', models.CharField(max_length=20)),
                ('discount', models.CharField(max_length=20)),
                ('image', models.URLField()),
                ('link', models.URLField()),
                ('alt_text', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('number_of_reviews', models.IntegerField()),
            ],
        ),
    ]