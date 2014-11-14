# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reading'
        db.create_table(u'weather_reading', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('wind', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('sky_conditions', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('temperature', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dewpoint', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('rh', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('pressure', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'weather', ['Reading'])


    def backwards(self, orm):
        # Deleting model 'Reading'
        db.delete_table(u'weather_reading')


    models = {
        u'weather.reading': {
            'Meta': {'object_name': 'Reading'},
            'dewpoint': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pressure': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rh': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'sky_conditions': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'temperature': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'wind': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        }
    }

    complete_apps = ['weather']