# Generated by Django 5.2 on 2025-04-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_screen', '0002_alter_customusermodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listnewsmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='Изображение'),
        ),
    ]
