from pathlib import Path
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Photo


class Command(BaseCommand):
    help = 'Loads data from specified json file url to database'

    def add_arguments(self, parser):
        parser.add_argument('place_description_urls', nargs='+', type=str)

    def handle(self, *args, **options):
        for place_description_url in options['place_description_urls']:
            response = requests.get(place_description_url)
            response.raise_for_status()
            place_details = response.json()
            place, created = Place.objects.get_or_create(
                title=place_details['title'],
                lat=place_details['coordinates']['lat'],
                lon=place_details['coordinates']['lng'],
                defaults={
                    'long_description': place_details['description_long'],
                    'short_description': place_details['description_short'],
                }
            )
            for position, photo_url in enumerate(
                    place_details['imgs'],
                    start=1):
                response = requests.get(photo_url)
                response.raise_for_status()
                photo, created = Photo.objects.get_or_create(
                    position=position,
                    place=place
                )
                filename = Path(urlparse(photo_url).path).name
                photo.image.save(
                    filename,
                    ContentFile(response.content),
                    save=True
                )
        self.stdout.write(self.style.SUCCESS('Place(s) successfully added!'))
