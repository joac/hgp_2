from django.contrib import admin
from .models import Photo, Video, Album, Tag, AlbumLink
from .forms import AlbumLinkForm
class AlbumLinkInline(admin.TabularInline):
    form = AlbumLinkForm
    model = AlbumLink
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('portrait', '__unicode__',)
    inlines = (AlbumLinkInline,)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('hacky_thumbnail', 'title', 'all_tags')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag)
