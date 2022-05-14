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


class Photo(models.Model):
    position = models.IntegerField('Позиция', db_index=True, default=0)
    image = models.ImageField('Изображение', upload_to='photos/')
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='photos',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['position']
        verbose_name = 'фотогафия'
        verbose_name_plural = 'фотографии'

    def __str__(self):
        return f'{self.place} - {self.position}'
