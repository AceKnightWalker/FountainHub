from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.urls import reverse
from .managers import PostManager
from django.db import models


class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Career', 'Career'),
        ('Campus', 'Campus'),
        ('Others', 'Others'),
        ('Tutorials', 'Tutorials'),
        ('Islam', 'Islam'),
        ('Interviews', 'Interviews'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='others')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(default='', blank=True, unique=True)
    text = RichTextUploadingField()
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    objects = PostManager()

    class Meta:
        ordering = ['-published_date']

    def save(self):
        self.published_date = timezone.now()
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('blog:details', kwargs={'slug': self.slug})


class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_blogname')
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return self.text
