from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self: 'Manufacturer') -> str:
        return f'{self.name} ({self.country})'


class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'driver'
        verbose_name_plural = 'drivers'
        ordering = ['username']

    def __str__(self: 'Driver') -> str:
        return f'{self.username} ({self.license_number})'


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name='cars', blank=True)

    class Meta:
        ordering = ['model']

    def __str__(self: 'Car') -> str:
        return f'{self.model} ({self.manufacturer.name})'
