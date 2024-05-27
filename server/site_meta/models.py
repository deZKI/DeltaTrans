from django.db import models

from utils.singleton import SingletonModel


class AboutUs(SingletonModel):
    description = models.TextField(verbose_name='Описание компании')

    favicon = models.FileField(verbose_name='Фавикон')
    name = models.CharField(max_length=255, verbose_name='Название компании')
    address = models.CharField(max_length=255, verbose_name='Адресс')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    logo = models.FileField(verbose_name='Логотип сайта')

    def __str__(self):
        return "О нас"

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'Информация о компании'


class AboutUsImage(models.Model):
    about_us = models.ForeignKey(AboutUs, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about/', verbose_name='Картинки')

    def __str__(self):
        return f"Картинка {self.about_us}"

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
