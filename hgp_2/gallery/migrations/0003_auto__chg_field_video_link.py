# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Video.link'
        db.alter_column(u'gallery_video', 'link', self.gf('embed_video.fields.EmbedVideoField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Video.link'
        db.alter_column(u'gallery_video', 'link', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        u'gallery.album': {
            'Meta': {'object_name': 'Album'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'resources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gallery.MediaResource']", 'symmetrical': 'False', 'through': u"orm['gallery.AlbumLink']", 'blank': 'True'})
        },
        u'gallery.albumlink': {
            'Meta': {'object_name': 'AlbumLink'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Album']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'resource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.MediaResource']"})
        },
        u'gallery.mediaresource': {
            'Meta': {'object_name': 'MediaResource'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gallery.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'gallery.photo': {
            'Meta': {'object_name': 'Photo', '_ormbases': [u'gallery.MediaResource']},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'mediaresource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['gallery.MediaResource']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'gallery.tag': {
            'Meta': {'object_name': 'Tag'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'resource': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gallery.MediaResource']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'gallery.video': {
            'Meta': {'object_name': 'Video', '_ormbases': [u'gallery.MediaResource']},
            'link': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'}),
            u'mediaresource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['gallery.MediaResource']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['gallery']