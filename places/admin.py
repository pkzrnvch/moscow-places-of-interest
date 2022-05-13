from django.contrib import admin

from places.models import Place, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    fields = ('image', 'position')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
