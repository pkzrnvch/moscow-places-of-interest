# Generated by Django 4.0.4 on 2022-05-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_photo_options_alter_place_long_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
    ]
