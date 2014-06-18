# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Credit'
        db.create_table(u'loans_credit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['banks.Bank'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('max_sum', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=2, blank=True)),
            ('min_sum', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=2, blank=True)),
            ('percent_years', self.gf('django.db.models.fields.DecimalField')(max_digits=100, decimal_places=2)),
            ('gasv', self.gf('django.db.models.fields.DecimalField')(max_digits=100, decimal_places=2)),
            ('term', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'loans', ['Credit'])


    def backwards(self, orm):
        # Deleting model 'Credit'
        db.delete_table(u'loans_credit')


    models = {
        u'banks.bank': {
            'Meta': {'object_name': 'Bank'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phones': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'loans.credit': {
            'Meta': {'object_name': 'Credit'},
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banks.Bank']"}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'gasv': ('django.db.models.fields.DecimalField', [], {'max_digits': '100', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_sum': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2', 'blank': 'True'}),
            'min_sum': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'percent_years': ('django.db.models.fields.DecimalField', [], {'max_digits': '100', 'decimal_places': '2'}),
            'term': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['loans']