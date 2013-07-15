# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Bookmark.created_at'
        db.alter_column(u'widgets_bookmark', 'created_at', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

        # Changing field 'Bookmark.updated_at'
        db.alter_column(u'widgets_bookmark', 'updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True))

    def backwards(self, orm):

        # Changing field 'Bookmark.created_at'
        db.alter_column(u'widgets_bookmark', 'created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Bookmark.updated_at'
        db.alter_column(u'widgets_bookmark', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    models = {
        u'widgets.bookmark': {
            'Meta': {'ordering': "['-updated_at']", 'object_name': 'Bookmark'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'widgets.quote': {
            'Meta': {'ordering': "['quoted_by']", 'object_name': 'Quote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quotation': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'quoted_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'use_it': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['widgets']