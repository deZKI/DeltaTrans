# Generated by Django 5.0.6 on 2024-05-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_meta', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutusimage',
            options={'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.AddField(
            model_name='aboutus',
            name='favicon',
            field=models.FileField(default=1, upload_to='', verbose_name='Фавикон'),
            preserve_default=False,
        ),
    ]
