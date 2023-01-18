from django.db import models

# Create your models here

class Clinic(models.Model):
    uslugi = models.CharField(verbose_name='Услуги', max_length=150, blank=True, default='')
    content = models.TextField(verbose_name='Содержание', blank=True, default='')
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=13, default='')

    def __str__(self):
        return f'{self.uslugi}'

    class Meta:
        verbose_name = 'Клиника'
        verbose_name_plural = 'Клиники'
        ordering = ['-pk',]
