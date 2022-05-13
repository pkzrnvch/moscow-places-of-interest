from django.urls import path
from places import views


urlpatterns = [
    path('<int:place_id>', views.place_detail_json)
]
