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


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table(u'widgets_quote')


    models = {
        u'widgets.quote': {
            'Meta': {'ordering': "['quoted_by']", 'object_name': 'Quote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quotation': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'quoted_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'use_it': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['widgets']