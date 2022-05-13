from django.http import JsonResponse
from places.models import Place, Photo
from django.shortcuts import get_object_or_404


def place_detail_json(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_photos = [photo.image.url for photo in place.photos.all()]
    place_details = {
        'title': place.title,
        'imgs': place_photos,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lon,
            'lat': place.lat
        }
    }
    return JsonResponse(
        place_details,
        json_dumps_params={'indent': 4, 'ensure_ascii': False}
    )
