# Generated by Django 2.2.7 on 2019-12-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20191209_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicename',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='services_img/', verbose_name='Изображение для страницы со всеми услугами (555 x 225)'),
        ),
    ]
