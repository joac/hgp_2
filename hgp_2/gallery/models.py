from django.db import models


class MediaResource(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    date_created = models.DateTimeField()
    tags = models.ManyToManyField('Tag')


class Photo(MediaResource):
    file = models.FileField(upload_to='photos')

class Video(MediaResource):
    file = models.URLField()

class Tag(models.Model):
    name = models.CharField(max_length=60)
    resource = models.ManyToManyField('MediaResource')
    date_created = models.DateTimeField()

class Album(models.Model):
    name = models.CharField(max_length=60)
    photos = models.ManyToManyField('MediaResource', through='AlbumLink')
    date_created = models.DateTimeField()

class AlbumLink(models.Model):
    album = models.ForeignKey('Album')
    resource = models.ForeignKey('MediaResource')
    order = models.IntegerField()
