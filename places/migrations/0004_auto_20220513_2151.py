# Generated by Django 3.2.13 on 2022-05-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_photo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='number',
        ),
        migrations.AddField(
            model_name='photo',
            name='position',
            field=models.IntegerField(default=11, verbose_name='Позиция'),
            preserve_default=False,
        ),
    ]
