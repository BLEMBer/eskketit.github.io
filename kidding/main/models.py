from django.db import models

class shoes(models.Model):
    title = models.CharField('Название пары' ,max_length=255)