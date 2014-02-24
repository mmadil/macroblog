# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'widgets_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'widgets', ['Category'])

        # Deleting field 'Bookmark.description'
        db.delete_column(u'widgets_bookmark', 'description')

        # Deleting field 'Bookmark.show'
        db.delete_column(u'widgets_bookmark', 'show')

        # Deleting field 'Bookmark.created_at'
        db.delete_column(u'widgets_bookmark', 'created_at')

        # Deleting field 'Bookmark.updated_at'
        db.delete_column(u'widgets_bookmark', 'updated_at')

        # Adding field 'Bookmark.tease'
        db.add_column(u'widgets_bookmark', 'tease',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Bookmark.status'
        db.add_column(u'widgets_bookmark', 'status',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'widgets_category')

        # Adding field 'Bookmark.description'
        db.add_column(u'widgets_bookmark', 'description',
                      self.gf('django.db.models.fields.TextField')(default=1, max_length=255),
                      keep_default=False)

        # Adding field 'Bookmark.show'
        db.add_column(u'widgets_bookmark', 'show',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Bookmark.created_at'
        db.add_column(u'widgets_bookmark', 'created_at',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=1, blank=True),
                      keep_default=False)

        # Adding field 'Bookmark.updated_at'
        db.add_column(u'widgets_bookmark', 'updated_at',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, default=1, blank=True),
                      keep_default=False)

        # Deleting field 'Bookmark.tease'
        db.delete_column(u'widgets_bookmark', 'tease')

        # Deleting field 'Bookmark.status'
        db.delete_column(u'widgets_bookmark', 'status')


    models = {
        u'widgets.bookmark': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Bookmark'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'tease': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'widgets.category': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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