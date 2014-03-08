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

        # Adding model 'Category'
        db.create_table(u'widgets_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'widgets', ['Category'])

        # Adding model 'Bookmark'
        db.create_table(u'widgets_bookmark', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('tease', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('status', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal(u'widgets', ['Bookmark'])

        # Adding M2M table for field categories on 'Bookmark'
        m2m_table_name = db.shorten_name(u'widgets_bookmark_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bookmark', models.ForeignKey(orm[u'widgets.bookmark'], null=False)),
            ('category', models.ForeignKey(orm[u'widgets.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bookmark_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table(u'widgets_quote')

        # Deleting model 'Category'
        db.delete_table(u'widgets_category')

        # Deleting model 'Bookmark'
        db.delete_table(u'widgets_bookmark')

        # Removing M2M table for field categories on 'Bookmark'
        db.delete_table(db.shorten_name(u'widgets_bookmark_categories'))


    models = {
        u'widgets.bookmark': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Bookmark'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['widgets.Category']", 'symmetrical': 'False'}),
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