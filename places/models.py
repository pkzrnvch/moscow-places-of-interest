from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = models.TextField('Подробное описание', blank=True)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return self.title
