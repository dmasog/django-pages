# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Reading.slug'
        db.add_column(u'weather_reading', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='raleigh', max_length=40),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Reading.slug'
        db.delete_column(u'weather_reading', 'slug')


    models = {
        u'weather.reading': {
            'Meta': {'object_name': 'Reading'},
            'dewpoint': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pressure': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rh': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sky_conditions': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'raleigh'", 'max_length': '40'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'temperature': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'wind': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        }
    }

    complete_apps = ['weather']