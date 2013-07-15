# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quote'
        db.create_table(u'widgets_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quotation', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('quoted_by', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('use_it', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'widgets', ['Quote'])

        # Adding model 'Bookmark'
        db.create_table(u'widgets_bookmark', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('show', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'widgets', ['Bookmark'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table(u'widgets_quote')

        # Deleting model 'Bookmark'
        db.delete_table(u'widgets_bookmark')


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