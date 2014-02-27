from django.db import models
from embed_video.fields import EmbedVideoField


class MediaResource(models.Model):
    title = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __unicode__(self):
        return self.title


class Photo(MediaResource):
    file = models.FileField(upload_to='photos')

    def hacky_thumbnail(self):
        return u"<img src='{0}' height='100px'/>".format(self.photo.file.url)

    hacky_thumbnail.allow_tags = True

    def all_tags(self):
        return u', '.join(self.tags.all())

    def __unicode__(self):
        return u"<img src='{0}' height='100px'/>".format(self.photo.file.url)


class Video(MediaResource):
    link = EmbedVideoField()

class Tag(models.Model):
    name = models.CharField(max_length=60)
    resource = models.ManyToManyField('MediaResource', blank=True)
    date_created = models.DateTimeField()

    def __unicode__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    resources = models.ManyToManyField('MediaResource', through='AlbumLink', blank=True)
    date_created = models.DateTimeField(blank=True)
    show_on_navbar = models.BooleanField(default=True)
    nav_order = models.PositiveIntegerField(blank=True)

    def portrait(self):
        img = self.get_first_resource()
        if img is not None:
            return u"<img src='{0}' height='100px'/>".format(img.photo.file.url)
        else:
            return u"Empty album"

    portrait.allow_tags = True



    def __unicode__(self):
        return self.name

    def get_first_resource(self):
        resources = self.get_all_resources()
        if resources:
            return resources[0]
        return None

    def get_all_resources(self):
        try:
            return self.resources.order_by('albumlink__order')
        except MediaResource.DoesNotExist:
            return None


class AlbumLink(models.Model):
    album = models.ForeignKey('Album')
    resource = models.ForeignKey('MediaResource')
    order = models.IntegerField()

    def __unicode__(self):
        return u"%s (%d) %s" % (self.album, self.order, self.resource)
