from django.contrib import admin
from .models import Photo, Video, Album, Tag, AlbumLink

class AlbumLinkInline(admin.TabularInline):
    model = AlbumLink
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    inlines = (AlbumLinkInline,)

admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag)
