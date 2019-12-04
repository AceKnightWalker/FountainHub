# Generated by Django 2.1.7 on 2019-12-04 22:23

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(null=True)),
                ('event_brief', ckeditor_uploader.fields.RichTextUploadingField()),
                ('venue', models.CharField(max_length=200)),
                ('organizer', models.CharField(max_length=75)),
                ('organizer_info', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]