from django.shortcuts import render
from places.models import Place, Photo
from django.urls import reverse


def fetch_all_places(request):
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
                    "detailsUrl": reverse('place_details', args=(place.pk,))
                }
            }
        )

    context = {'places_geojson': {
        "type": "FeatureCollection",
        "features": features,
    }}
    return render(request, 'index.html', context=context)
