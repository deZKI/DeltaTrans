# Generated by Django 5.0.6 on 2024-05-27 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание компании')),
                ('name', models.CharField(max_length=255, verbose_name='Название компании')),
                ('address', models.CharField(max_length=255, verbose_name='Адресс')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('logo', models.FileField(upload_to='', verbose_name='Логотип сайта')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'Информация о компании',
            },
        ),
        migrations.CreateModel(
            name='AboutUsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/', verbose_name='Картинки')),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='site_meta.aboutus')),
            ],
        ),
    ]