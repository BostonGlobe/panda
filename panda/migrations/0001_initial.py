# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import panda.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0002_auto_20180425_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateField(help_text='The date this activity was recorded.', verbose_name='when', auto_now=True)),
            ],
            options={
                'verbose_name': 'ActivityLog',
                'verbose_name_plural': 'ActivityLogs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=256, verbose_name='slug')),
                ('name', models.CharField(help_text='Category name.', max_length=64, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=256, verbose_name='slug')),
                ('name', models.CharField(help_text='User-supplied dataset name.', max_length=256, verbose_name='name')),
                ('description', models.TextField(help_text='User-supplied dataset description.', verbose_name='description', blank=True)),
                ('column_schema', panda.fields.JSONField(default=None, help_text='Metadata about columns.', null=True, verbose_name='column_schema')),
                ('sample_data', panda.fields.JSONField(default=None, help_text='Example data rows from the dataset.', null=True, verbose_name='sample_data')),
                ('row_count', models.IntegerField(help_text='The number of rows in this dataset. Null if no data has been added/imported.', null=True, verbose_name='row_count', blank=True)),
                ('creation_date', models.DateTimeField(help_text='The date this dataset was initially created.', null=True, verbose_name='creation_date')),
                ('last_modified', models.DateTimeField(default=None, help_text='When, if ever, was this dataset last modified via the API?', null=True, verbose_name='last_modified', blank=True)),
                ('last_modification', models.TextField(default=None, help_text='Description of the last modification made to this Dataset.', null=True, verbose_name='last_modification', blank=True)),
                ('locked', models.BooleanField(default=False, help_text='Is this table locked for writing?', verbose_name='locked')),
                ('locked_at', models.DateTimeField(default=None, help_text='Time this dataset was last locked.', null=True, verbose_name='locked_at')),
                ('related_links', panda.fields.JSONField(default=[])),
                ('categories', models.ManyToManyField(related_name=b'datasets', to='panda.Category', blank=True, help_text='Categories containing this Dataset.', null=True, verbose_name='categories')),
            ],
            options={
                'ordering': ['-creation_date'],
                'verbose_name': 'Dataset',
                'verbose_name_plural': 'Datasets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(help_text='Filename as stored in PANDA.', max_length=256, verbose_name='filename')),
                ('original_filename', models.CharField(help_text='Filename as originally uploaded.', max_length=256, verbose_name='original_filename')),
                ('size', models.IntegerField(help_text='Size of the file in bytes.', verbose_name='size')),
                ('creation_date', models.DateTimeField(help_text='The date this file was uploaded.', verbose_name='creation_date')),
                ('title', models.TextField(help_text='A user-friendly name for this file.', max_length=256, verbose_name='title')),
                ('data_type', models.CharField(help_text='The type of this file, if known.', max_length=4, null=True, verbose_name='data_type', blank=True)),
                ('encoding', models.CharField(default=b'utf-8', help_text='The character encoding of this file. Defaults to utf-8', max_length=32, verbose_name='encoding')),
                ('dialect', panda.fields.JSONField(help_text='Description of the formatting of this file.', null=True, verbose_name='dialect')),
                ('columns', panda.fields.JSONField(help_text='A list of names for the columns in this upload.', null=True, verbose_name='columns')),
                ('sample_data', panda.fields.JSONField(help_text='Example data from this file.', null=True, verbose_name='sample_data')),
                ('guessed_types', panda.fields.JSONField(help_text='Column types guessed based on a sample of data.', null=True, verbose_name='guessed_types')),
                ('imported', models.BooleanField(default=False, help_text='Has this upload ever been imported into its parent dataset.', verbose_name='imported')),
                ('deletable', models.BooleanField(default=True, help_text='Can this data upload be deleted? False for uploads prior to 1.0.', verbose_name='deletable')),
                ('dataset', models.ForeignKey(related_name=b'data_uploads', verbose_name='dataset', to='panda.Dataset', help_text='The dataset this upload is associated with.', null=True)),
            ],
            options={
                'ordering': ['creation_date'],
                'verbose_name': 'DataUpload',
                'verbose_name_plural': 'DataUploads',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(help_text='Filename as stored in PANDA.', max_length=256, verbose_name='filename')),
                ('original_filename', models.CharField(help_text='Filename as originally uploaded.', max_length=256, verbose_name='original_filename')),
                ('size', models.IntegerField(help_text='Size of the file in bytes.', verbose_name='size')),
                ('creation_date', models.DateTimeField(help_text='The date this file was uploaded.', verbose_name='creation_date')),
                ('title', models.TextField(help_text='A user-friendly name for this file.', max_length=256, verbose_name='title')),
                ('dataset', models.ForeignKey(related_name=b'exports', verbose_name='dataset', to='panda.Dataset', help_text='The dataset this export is from.', null=True)),
            ],
            options={
                'ordering': ['creation_date'],
                'verbose_name': 'Export',
                'verbose_name_plural': 'Exports',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(help_text='The message to deliver.', verbose_name='message')),
                ('type', models.CharField(default=b'Info', help_text='The type of message: info, warning or error', max_length=16, verbose_name='type', choices=[(b'Info', 'Info'), (b'Warning', 'Warning'), (b'Error', 'Error')])),
                ('sent_at', models.DateTimeField(help_text='When this notification was created', verbose_name='sent_at', auto_now=True)),
                ('read_at', models.DateTimeField(default=None, help_text='When this notification was read by the user.', null=True, verbose_name='read_at', blank=True)),
                ('url', models.URLField(default=None, null=True, verbose_name='url', help_text='A url to link to when displaying this notification.')),
            ],
            options={
                'ordering': ['-sent_at'],
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(help_text='Filename as stored in PANDA.', max_length=256, verbose_name='filename')),
                ('original_filename', models.CharField(help_text='Filename as originally uploaded.', max_length=256, verbose_name='original_filename')),
                ('size', models.IntegerField(help_text='Size of the file in bytes.', verbose_name='size')),
                ('creation_date', models.DateTimeField(help_text='The date this file was uploaded.', verbose_name='creation_date')),
                ('title', models.TextField(help_text='A user-friendly name for this file.', max_length=256, verbose_name='title')),
                ('dataset', models.ForeignKey(related_name=b'related_uploads', verbose_name='dataset', to='panda.Dataset', help_text='The dataset this upload is associated with.')),
            ],
            options={
                'ordering': ['creation_date'],
                'verbose_name': 'RelatedUpload',
                'verbose_name_plural': 'RelatedUploads',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SearchLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.CharField(help_text='The search query that was executed', max_length=4096, verbose_name='query')),
                ('when', models.DateTimeField(help_text='The date and time this search was logged.', verbose_name='when', auto_now=True)),
                ('dataset', models.ForeignKey(related_name=b'searches', default=None, to='panda.Dataset', help_text='The data set searched, or null if all were searched.', null=True, verbose_name='dataset')),
            ],
            options={
                'verbose_name': 'SearchLog',
                'verbose_name_plural': 'SearchLogs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SearchSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.CharField(help_text='The search query to executed.', max_length=256, verbose_name='query')),
                ('query_url', models.CharField(help_text='Query encoded for URL.', max_length=256, verbose_name='query_url')),
                ('query_human', models.TextField(help_text='Human-readable description of the query being run.', verbose_name='query_human')),
                ('last_run', models.DateTimeField(help_text='The last time this search this was run.', verbose_name='last_run', auto_now=True)),
                ('category', models.ForeignKey(related_name=b'search_subscriptions', default=None, to='panda.Category', help_text='A category to be searched or null if all are to be searched.', null=True, verbose_name='category')),
                ('dataset', models.ForeignKey(related_name=b'search_subscriptions', default=None, to='panda.Dataset', help_text='The dataset to be searched or null if all are to be searched.', null=True, verbose_name='dataset')),
            ],
            options={
                'verbose_name': 'SearchSubscription',
                'verbose_name_plural': 'SearchSubscriptions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(help_text='Identifying name for this task.', max_length=255, verbose_name='task_name')),
                ('task_description', models.TextField(help_text='Description of the task.', verbose_name='task_description')),
                ('status', models.CharField(default=b'PENDING', help_text='Current state of this task.', max_length=50, verbose_name='status', choices=[(b'FAILURE', b'FAILURE'), (b'PENDING', b'PENDING'), (b'RECEIVED', b'RECEIVED'), (b'RETRY', b'RETRY'), (b'REVOKED', b'REVOKED'), (b'STARTED', b'STARTED'), (b'SUCCESS', b'SUCCESS'), (b'ABORTED', b'ABORTED'), (b'ABORT REQUESTED', b'ABORT REQUESTED')])),
                ('message', models.CharField(help_text='A human-readable message indicating the progress of this task.', max_length=255, verbose_name='message', blank=True)),
                ('start', models.DateTimeField(help_text='Date and time that this task began processing.', null=True, verbose_name='start')),
                ('end', models.DateTimeField(help_text='Date and time that this task ceased processing (either complete or failed).', null=True, verbose_name='end')),
                ('traceback', models.TextField(default=None, help_text='Traceback that exited this task, if it failed.', null=True, verbose_name='traceback', blank=True)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40, null=True, verbose_name='activation_key', blank=True)),
                ('activation_key_expiration', models.DateTimeField(verbose_name='activation_key_expiration')),
                ('show_login_help', models.BooleanField(default=True, help_text=b'This field is no longer used.', verbose_name='show_login_help')),
            ],
            options={
                'verbose_name': 'UserProfile',
                'verbose_name_plural': 'UserProfiles',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dataset',
            name='current_task',
            field=models.ForeignKey(blank=True, to='panda.TaskStatus', help_text='The currently executed or last finished task related to this dataset.', null=True, verbose_name='current_task'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataset',
            name='initial_upload',
            field=models.ForeignKey(related_name=b'initial_upload_for', blank=True, to='panda.DataUpload', help_text='The data upload used to create this dataset, if any was used.', null=True, verbose_name='initial_upload'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='UserProxy',
            fields=[
            ],
            options={
                'verbose_name': 'User',
                'proxy': True,
                'verbose_name_plural': 'Users',
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='activitylog',
            name='user',
            field=models.ForeignKey(related_name=b'activity_logs', verbose_name='user', to='panda.UserProxy', help_text='The user who was active.'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='activitylog',
            unique_together=set([('user', 'when')]),
        ),
        migrations.AddField(
            model_name='dataset',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, to='panda.UserProxy', help_text='The user, if any, who last modified this dataset.', null=True, verbose_name='last_modified_by'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataset',
            name='creator',
            field=models.ForeignKey(related_name=b'datasets', verbose_name='creator', to='panda.UserProxy', help_text='The user who created this dataset.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataupload',
            name='creator',
            field=models.ForeignKey(verbose_name='creator', to='panda.UserProxy', help_text='The user who uploaded this file.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='export',
            name='creator',
            field=models.ForeignKey(verbose_name='creator', to='panda.UserProxy', help_text='The user who uploaded this file.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(related_name=b'notifications', verbose_name='recipient', to='panda.UserProxy', help_text='The user who should receive this notification.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relatedupload',
            name='creator',
            field=models.ForeignKey(verbose_name='creator', to='panda.UserProxy', help_text='The user who uploaded this file.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='searchlog',
            name='user',
            field=models.ForeignKey(related_name=b'search_logs', verbose_name='user', to='panda.UserProxy', help_text='The user who executed the search.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='searchsubscription',
            name='user',
            field=models.ForeignKey(related_name=b'search_subscriptions', verbose_name='user', to='panda.UserProxy', help_text='The user who subscribed to the search.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskstatus',
            name='creator',
            field=models.ForeignKey(related_name=b'tasks', verbose_name='creator', to='panda.UserProxy', help_text='The user who initiated this task.', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(verbose_name='user', to='panda.UserProxy'),
            preserve_default=True,
        ),
    ]
