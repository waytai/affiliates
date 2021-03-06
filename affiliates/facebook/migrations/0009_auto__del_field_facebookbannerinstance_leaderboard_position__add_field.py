# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'FacebookBannerInstance.leaderboard_position'
        db.delete_column('facebook_facebookbannerinstance', 'leaderboard_position')

        # Adding field 'FacebookUser.leaderboard_position'
        db.add_column('facebook_facebookuser', 'leaderboard_position',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'FacebookBannerInstance.leaderboard_position'
        db.add_column('facebook_facebookbannerinstance', 'leaderboard_position',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Deleting field 'FacebookUser.leaderboard_position'
        db.delete_column('facebook_facebookuser', 'leaderboard_position')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'facebook.facebookaccountlink': {
            'Meta': {'object_name': 'FacebookAccountLink'},
            'activation_code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'affiliates_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'account_links'", 'to': "orm['auth.User']"}),
            'facebook_user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'_account_link'", 'unique': 'True', 'to': "orm['facebook.FacebookUser']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'facebook.facebookbanner': {
            'Meta': {'object_name': 'FacebookBanner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Banner'", 'unique': 'True', 'max_length': '255'})
        },
        'facebook.facebookbannerinstance': {
            'Meta': {'object_name': 'FacebookBannerInstance'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facebook.FacebookBanner']"}),
            'can_be_an_ad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'total_clicks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'banner_instance_set'", 'to': "orm['facebook.FacebookUser']"})
        },
        'facebook.facebookbannerlocale': {
            'Meta': {'object_name': 'FacebookBannerLocale'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locale_set'", 'to': "orm['facebook.FacebookBanner']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('affiliates.shared.models.LocaleField', [], {'default': "'en-US'", 'max_length': '32'})
        },
        'facebook.facebookclickstats': {
            'Meta': {'object_name': 'FacebookClickStats'},
            'banner_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facebook.FacebookBannerInstance']"}),
            'clicks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hour': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 8, 16, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'facebook.facebookuser': {
            'Meta': {'object_name': 'FacebookUser'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'primary_key': 'True'}),
            'leaderboard_position': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        }
    }

    complete_apps = ['facebook']
