# Generated by Django 2.2.6 on 2019-11-19 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20191119_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicename',
            name='price',
        ),
    ]
