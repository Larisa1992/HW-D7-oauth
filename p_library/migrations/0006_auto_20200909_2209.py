# Generated by Django 2.2.6 on 2020-09-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_auto_20200830_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='user_cover/%Y/%m/%d', verbose_name='Обложка книги'),
        ),
    ]
