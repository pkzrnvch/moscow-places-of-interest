from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places.models import Place, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    readonly_fields = ('preview_image',)
    fields = ('image', 'preview_image', 'position')

    def preview_image(self, obj):
        return format_html(
            '<img src="{}" width=auto height=200px />',
            obj.image.url,
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
