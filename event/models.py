from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Event(models.Model):
    thumbnail = models.ImageField()
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(default='', blank=True, unique=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    time = models.TimeField(null=True)
    event_brief = RichTextUploadingField()
    venue = models.CharField(max_length=200)
    organizer = models.CharField(max_length=75)
    organizer_info = RichTextUploadingField()

    class Meta:
        ordering = ['-start_date']

    def save(self):
        self.slug = slugify(self.title)
        super(Event, self).save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
