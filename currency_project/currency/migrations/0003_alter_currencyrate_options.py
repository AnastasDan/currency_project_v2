# Generated by Django 3.2.3 on 2024-02-15 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_auto_20240215_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currencyrate',
            options={'ordering': ('-date',), 'verbose_name': 'Курс валюты', 'verbose_name_plural': 'Курсы валют'},
        ),
    ]