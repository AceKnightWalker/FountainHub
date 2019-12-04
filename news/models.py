from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    picture = models.ImageField(blank=True)
    headline = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(default='', blank=True, unique=True)
    content = RichTextUploadingField()

    class Meta:
        ordering = ['-pub_date']

    def save(self):
        self.slug = slugify(self.headline)
        super(Article, self).save()

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_newsname')
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return self.text
