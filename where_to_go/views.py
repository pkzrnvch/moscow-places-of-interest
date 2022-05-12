from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place, Photo


def index(request):
    features = []
    places = Place.objects.all()
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lon, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.pk,
                    "detailsUrl": "/static/places/moscow_legends.json"
                }
            }
        )

    places = {
        "type": "FeatureCollection",
        "features": features
    }

    context = {'places_geojson': places}
    return render(request, 'index.html', context=context)
