# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MediaResource'
        db.create_table(u'gallery_mediaresource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'gallery', ['MediaResource'])

        # Adding M2M table for field tags on 'MediaResource'
        m2m_table_name = db.shorten_name(u'gallery_mediaresource_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mediaresource', models.ForeignKey(orm[u'gallery.mediaresource'], null=False)),
            ('tag', models.ForeignKey(orm[u'gallery.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mediaresource_id', 'tag_id'])

        # Adding model 'Photo'
        db.create_table(u'gallery_photo', (
            (u'mediaresource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['gallery.MediaResource'], unique=True, primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'gallery', ['Photo'])

        # Adding model 'Video'
        db.create_table(u'gallery_video', (
            (u'mediaresource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['gallery.MediaResource'], unique=True, primary_key=True)),
            ('file', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'gallery', ['Video'])

        # Adding model 'Tag'
        db.create_table(u'gallery_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'gallery', ['Tag'])

        # Adding M2M table for field resource on 'Tag'
        m2m_table_name = db.shorten_name(u'gallery_tag_resource')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'gallery.tag'], null=False)),
            ('mediaresource', models.ForeignKey(orm[u'gallery.mediaresource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'mediaresource_id'])

        # Adding model 'Album'
        db.create_table(u'gallery_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'gallery', ['Album'])

        # Adding model 'AlbumLink'
        db.create_table(u'gallery_albumlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Album'])),
            ('resource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.MediaResource'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'gallery', ['AlbumLink'])


    def backwards(self, orm):
        # Deleting model 'MediaResource'
        db.delete_table(u'gallery_mediaresource')

        # Removing M2M table for field tags on 'MediaResource'
        db.delete_table(db.shorten_name(u'gallery_mediaresource_tags'))

        # Deleting model 'Photo'
        db.delete_table(u'gallery_photo')

        # Deleting model 'Video'
        db.delete_table(u'gallery_video')

        # Deleting model 'Tag'
        db.delete_table(u'gallery_tag')

        # Removing M2M table for field resource on 'Tag'
        db.delete_table(db.shorten_name(u'gallery_tag_resource'))

        # Deleting model 'Album'
        db.delete_table(u'gallery_album')

        # Deleting model 'AlbumLink'
        db.delete_table(u'gallery_albumlink')


    models = {
        u'gallery.album': {
            'Meta': {'object_name': 'Album'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gallery.MediaResource']", 'through': u"orm['gallery.AlbumLink']", 'symmetrical': 'False'})
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
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gallery.Tag']", 'symmetrical': 'False'}),
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
            'resource': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gallery.MediaResource']", 'symmetrical': 'False'})
        },
        u'gallery.video': {
            'Meta': {'object_name': 'Video', '_ormbases': [u'gallery.MediaResource']},
            'file': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'mediaresource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['gallery.MediaResource']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['gallery']