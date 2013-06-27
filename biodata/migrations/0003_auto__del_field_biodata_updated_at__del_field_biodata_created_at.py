# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Biodata.updated_at'
        db.delete_column(u'biodata_biodata', 'updated_at')

        # Deleting field 'Biodata.created_at'
        db.delete_column(u'biodata_biodata', 'created_at')


    def backwards(self, orm):
        # Adding field 'Biodata.updated_at'
        db.add_column(u'biodata_biodata', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=1, blank=True),
                      keep_default=False)

        # Adding field 'Biodata.created_at'
        db.add_column(u'biodata_biodata', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=1, blank=True),
                      keep_default=False)


    models = {
        u'biodata.biodata': {
            'Meta': {'ordering': "['order']", 'object_name': 'Biodata'},
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'biodata.project': {
            'Meta': {'ordering': "['heading']", 'object_name': 'Project'},
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['biodata']