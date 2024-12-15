from django.db import models
# Create your models here.


class ListNewsModel(models.Model):
    name = models.CharField(verbose_name='Заголовок', max_length=255)

    class Meta:
        verbose_name = 'Данные Новости'
        verbose_name_plural = 'Данные Новостей'