from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Photo


class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Photo
    readonly_fields = ('preview_image',)
    fields = ('position', 'image', 'preview_image')
    ordering = ('position',)

    def preview_image(self, obj):
        return format_html(
            '<img src="{}" width=auto height=200px />',
            obj.image.url,
        )

    def get_extra(self, request, obj=None, **kwargs):
        return 0


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        return format_html(
            '<img src="{}" width=auto height=200px />',
            obj.image.url,
        )
