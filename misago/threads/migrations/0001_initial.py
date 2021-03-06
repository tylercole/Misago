# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Thread'
        db.create_table(u'threads_thread', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('forum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forums.Forum'])),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('replies', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('replies_reported', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('replies_moderated', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('replies_deleted', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('merges', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('score', self.gf('django.db.models.fields.PositiveIntegerField')(default=30)),
            ('upvotes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('downvotes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('start_post', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['threads.Post'])),
            ('start_poster', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('start_poster_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start_poster_slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('start_poster_style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_post', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['threads.Post'])),
            ('last_poster', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['users.User'])),
            ('last_poster_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_poster_slug', self.gf('django.db.models.fields.SlugField')(max_length=255, null=True, blank=True)),
            ('last_poster_style', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('moderated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'threads', ['Thread'])

        # Adding model 'Post'
        db.create_table(u'threads_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('forum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forums.Forum'])),
            ('thread', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['threads.Thread'])),
            ('merge', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('agent', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('post', self.gf('django.db.models.fields.TextField')()),
            ('post_preparsed', self.gf('django.db.models.fields.TextField')()),
            ('upvotes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('downvotes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('checkpoints', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('edits', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('edit_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('edit_reason', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('edit_user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, on_delete=models.SET_NULL, to=orm['users.User'])),
            ('edit_user_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('edit_user_slug', self.gf('django.db.models.fields.SlugField')(max_length=255, null=True, blank=True)),
            ('reported', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('moderated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('protected', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'threads', ['Post'])

        # Adding M2M table for field mentions on 'Post'
        db.create_table(u'threads_post_mentions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'threads.post'], null=False)),
            ('user', models.ForeignKey(orm[u'users.user'], null=False))
        ))
        db.create_unique(u'threads_post_mentions', ['post_id', 'user_id'])

        # Adding model 'Karma'
        db.create_table(u'threads_karma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('forum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forums.Forum'])),
            ('thread', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['threads.Thread'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['threads.Post'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user_slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('agent', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'threads', ['Karma'])

        # Adding model 'Change'
        db.create_table(u'threads_change', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('forum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forums.Forum'])),
            ('thread', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['threads.Thread'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['threads.Post'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user_slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('agent', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('thread_name_new', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('thread_name_old', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('post_content', self.gf('django.db.models.fields.TextField')()),
            ('size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('change', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'threads', ['Change'])

        # Adding model 'Checkpoint'
        db.create_table(u'threads_checkpoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('forum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forums.Forum'])),
            ('thread', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['threads.Thread'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['threads.Post'])),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user_slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('agent', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'threads', ['Checkpoint'])


    def backwards(self, orm):
        # Deleting model 'Thread'
        db.delete_table(u'threads_thread')

        # Deleting model 'Post'
        db.delete_table(u'threads_post')

        # Removing M2M table for field mentions on 'Post'
        db.delete_table('threads_post_mentions')

        # Deleting model 'Karma'
        db.delete_table(u'threads_karma')

        # Deleting model 'Change'
        db.delete_table(u'threads_change')

        # Deleting model 'Checkpoint'
        db.delete_table(u'threads_checkpoint')


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
        u'threads.change': {
            'Meta': {'object_name': 'Change'},
            'agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'change': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forums.Forum']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['threads.Post']"}),
            'post_content': ('django.db.models.fields.TextField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['threads.Thread']"}),
            'thread_name_new': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'thread_name_old': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'threads.checkpoint': {
            'Meta': {'object_name': 'Checkpoint'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forums.Forum']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['threads.Post']"}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['threads.Thread']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'threads.karma': {
            'Meta': {'object_name': 'Karma'},
            'agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forums.Forum']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['threads.Post']"}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['threads.Thread']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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

    complete_apps = ['threads']