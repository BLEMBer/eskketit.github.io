# Generated by Django 4.1.1 on 2023-10-09 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='shoes',
            options={'verbose_name': 'Обувь', 'verbose_name_plural': 'Обувь'},
        ),
    ]