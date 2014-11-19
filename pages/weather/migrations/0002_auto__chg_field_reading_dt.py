# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Reading.dt'
        db.alter_column(u'weather_reading', 'dt', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'Reading.dt'
        db.alter_column(u'weather_reading', 'dt', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        u'weather.reading': {
            'Meta': {'object_name': 'Reading'},
            'dewpoint': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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