from django.urls import path
from places import views


urlpatterns = [
    path('<int:place_id>', views.place_details_json, name='place_details'),
]
