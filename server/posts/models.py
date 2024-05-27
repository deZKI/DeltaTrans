from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок новости')
    content = models.TextField(verbose_name='Содержание новости')
    image = models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
