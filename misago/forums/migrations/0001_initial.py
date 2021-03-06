# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Forum'
        db.create_table(u'forums_forum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['forums.Forum'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_preparsed', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('threads', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('threads_delta', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('posts', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('posts_delta', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('redirects', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('redirects_delta', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('last_thread', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['threads.Thread'])),
            ('last_thread_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_thread_slug', self.gf('django.db.models.fields.SlugField')(max_length=255, null=True, blank=True)),
            ('last_thread_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_poster', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['users.User'])),
            ('last_poster_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_poster_slug', self.gf('django.db.models.fields.SlugField')(max_length=255, null=True, blank=True)),
            ('last_poster_style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('prune_start', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('prune_last', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('redirect', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('attrs', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('show_details', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'forums', ['Forum'])


    def backwards(self, orm):
        # Deleting model 'Forum'
        db.delete_table(u'forums_forum')


    models = {
        u'forums.forum': {
            'Meta': {'object_name': 'Forum'},
            'attrs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_preparsed': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_poster': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['users.User']"}),
            'last_poster_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_poster_slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_poster_style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_thread': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['threads.Thread']"}),
            'last_thread_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_thread_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_thread_slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['forums.Forum']"}),
            'posts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'posts_delta': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'prune_last': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'prune_start': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'redirect': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'redirects': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'redirects_delta': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'show_details': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'threads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'threads_delta': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'ranks.rank': {
            'Meta': {'object_name': 'Rank'},
            'as_tab': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'criteria': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'on_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'special': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'roles.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'permissions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'threads.post': {
            'Meta': {'object_name': 'Post'},
            'agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'checkpoints': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'downvotes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'edit_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'edit_reason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'edit_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['users.User']"}),
            'edit_user_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'edit_user_slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'edits': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forums.Forum']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'mentions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mention_set'", 'symmetrical': 'False', 'to': u"orm['users.User']"}),
            'merge': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'moderated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'post': ('django.db.models.fields.TextField', [], {}),
            'post_preparsed': ('django.db.models.fields.TextField', [], {}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['threads.Thread']"}),
            'upvotes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'threads.thread': {
            'Meta': {'object_name': 'Thread'},
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'downvotes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forums.Forum']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.DateTimeField', [], {}),
            'last_post': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['threads.Post']"}),
            'last_poster': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['users.User']"}),
            'last_poster_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_poster_slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_poster_style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'merges': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'moderated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'replies': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'replies_deleted': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'replies_moderated': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'replies_reported': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'start_post': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['threads.Post']"}),
            'start_poster': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'start_poster_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_poster_slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'start_poster_style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'upvotes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'acl_key': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'activation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'alerts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'alerts_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'allow_pms': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'avatar_ban': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'avatar_ban_reason_admin': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'avatar_ban_reason_user': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'avatar_image': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'avatar_original': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'avatar_temp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'avatar_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'email_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'followers': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'following': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'follows': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'follows_set'", 'symmetrical': 'False', 'to': u"orm['users.User']"}),
            'hide_activity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignores': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'ignores_set'", 'symmetrical': 'False', 'to': u"orm['users.User']"}),
            'is_team': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'join_agent': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'join_date': ('django.db.models.fields.DateTimeField', [], {}),
            'join_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'karma_given_n': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'karma_given_p': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'karma_n': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'karma_p': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'last_agent': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'last_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'last_post': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_search': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_sync': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password_date': ('django.db.models.fields.DateTimeField', [], {}),
            'posts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'rank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ranks.Rank']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'ranking': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'receive_newsletters': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['roles.Role']", 'symmetrical': 'False'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'signature': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'signature_ban': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'signature_ban_reason_admin': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'signature_ban_reason_user': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'signature_preparsed': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'subscribe_reply': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'subscribe_start': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'threads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'utc'", 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['forums']