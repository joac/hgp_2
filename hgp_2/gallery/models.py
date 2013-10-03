from django.db import models
from embed_video.fields import EmbedVideoField


class MediaResource(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    date_created = models.DateTimeField()
    tags = models.ManyToManyField('Tag', blank=True)

    def __unicode__(self):
        return self.title

class Photo(MediaResource):
    file = models.FileField(upload_to='photos')


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
    resources = models.ManyToManyField('MediaResource', through='AlbumLink', blank=True)
    date_created = models.DateTimeField()

    def __unicode__(self):
        return self.name

    def get_first_resource(self):
        return self.get_all_resources[0]

    def get_all_resources(self):
        return self.resources.order_by('albumlink__order')


class AlbumLink(models.Model):
    album = models.ForeignKey('Album')
    resource = models.ForeignKey('MediaResource')
    order = models.IntegerField()

    def __unicode__(self):
        return u"%s (%d) %s" % (self.album, self.order, self.resource)

