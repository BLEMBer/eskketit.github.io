from django.db import models


class shoes(models.Model):
    title = models.CharField('Название пары', max_length=255)
    content = models.TextField('Цена', blank=True)
    content1 = models.TextField('Артикул', blank=6)

    def __str__(self):
            return self.title

class order(models.Model):
    title1 = models.CharField('ФИО', max_length=100)
    date = models.DateTimeField('Дата создания заказа', auto_now_add=True)
    order = models.TextField('Состав заказа')

